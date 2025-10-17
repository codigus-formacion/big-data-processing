from mrjob.job import MRJob
from mrjob.step import MRStep
import csv
import io

class MRTeamStatistics(MRJob):
    """
    Análisis deportivo usando MapReduce con MRJob
    Calcula estadísticas por equipo de fútbol:
    - Promedio de goles por minuto jugado por equipo
    - Total de goles y minutos por equipo
    """

    def steps(self):
        return [
            MRStep(mapper=self.mapper_process_player,
                   combiner=self.combiner_sum_statistics,
                   reducer=self.reducer_calculate_averages),
            MRStep(reducer=self.reducer_find_best_team)
        ]

    def mapper_process_player(self, _, line):
        """
        Procesa cada línea del CSV y extrae información del jugador
        Emite (equipo, (contribuciones, minutos_jugados))
        """
        if line.startswith('name'):  # Saltar header
            return
        
        try:
            row = line.split(',')

            team = row[1]
            goals = int(row[3])
            assists = int(row[4])
            minutes_played = int(row[5])
            
            # Emitir estadísticas por equipo
            yield (team, {
                'goals': goals,
                'assists': assists,
                'minutes': minutes_played,
                'players': 1
            })
            
        except (ValueError, IndexError) as e:
            # Ignorar líneas con formato incorrecto
            pass

    def combiner_sum_statistics(self, team, statistics):
        """
        Combina estadísticas parciales por equipo
        """
        total_goals = 0
        total_assists = 0
        total_minutes = 0
        total_players = 0
        
        for stats in statistics:
            total_goals += stats['goals']
            total_assists += stats['assists']
            total_minutes += stats['minutes']
            total_players += stats['players']
        
        yield (team, {
            'goals': total_goals,
            'assists': total_assists,
            'minutes': total_minutes,
            'players': total_players
        })

    def reducer_calculate_averages(self, team, statistics):
        """
        Calcula promedios y métricas finales por equipo
        """
        total_goals = 0
        total_assists = 0
        total_minutes = 0
        total_players = 0
        
        for stats in statistics:
            total_goals += stats['goals']
            total_assists += stats['assists']
            total_minutes += stats['minutes']
            total_players += stats['players']
        
        # Calcular métricas
        contributions_per_minute = (total_goals + total_assists) / total_minutes if total_minutes > 0 else 0
        goals_per_minute = total_goals / total_minutes if total_minutes > 0 else 0
        
        # Emitir para encontrar el mejor equipo
        yield (None, {
            'team': team,
            'players': total_players,
            'goals': total_goals,
            'assists': total_assists,
            'contributions_per_minute': contributions_per_minute,
            'goals_per_minute': goals_per_minute
        })

    def reducer_find_best_team(self, _, team_stats):
        """
        Encuentra el equipo con mejor rendimiento ofensivo y muestra todas las estadísticas
        """
        teams = list(team_stats)
        
        sorted_teams = sorted(teams, key=lambda x: x['contributions_per_minute'], reverse=True)

        # Mostrar todas las estadísticas ordenadas
        for i, team in enumerate(sorted_teams, 1):
            yield (f"#{i} {team['team']:<25}", {
                'players': team['players'],
                'goals': team['goals'],
                'assists': team['assists'],
                'contributions_per_minute': f"{team['contributions_per_minute']:.4f}",
                'goals_per_minute': f"{team['goals_per_minute']:.4f}"
            })

if __name__ == '__main__':
    MRTeamStatistics.run()
       