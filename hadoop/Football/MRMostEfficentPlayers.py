from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMostEfficientPlayers(MRJob):
    """
    Análisis para encontrar los jugadores más eficientes
    Calcula la eficiencia ofensiva por minuto jugado
    """

    def steps(self):
        return [
            MRStep(mapper=self.mapper_process_individual_player,
                   reducer=self.reducer_player_ranking)
        ]

    def mapper_process_individual_player(self, _, line):
        """
        Procesa cada jugador y calcula su eficiencia
        """
        if line.startswith('name'):  # Saltar header
            return
        
        try:
            row = line.split(',')
            
            name = row[0]
            team = row[1]
            position = row[2]
            goals = int(row[3])
            assists = int(row[4])
            minutes_played = int(row[5])
            
            if minutes_played > 0:
                efficiency = ((goals + assists) * 90) / minutes_played
                
                yield (None, {
                    'name': name,
                    'team': team,
                    'position': position,
                    'goals': goals,
                    'assists': assists,
                    'minutes': minutes_played,
                    'efficiency': efficiency
                })
                
        except (ValueError, IndexError):
            pass

    def reducer_player_ranking(self, _, players):
        """
        Encuentra los jugadores más eficientes
        """
        player_list = list(players)
        
        # Ordenar por eficiencia
        sorted_players = sorted(player_list, key=lambda x: x['efficiency'], reverse=True)
        
        # Emitir los 10 jugadores más eficientes
        for i, player in enumerate(sorted_players[:10], 1):
            yield (f"{player['name']:<20}", f"{player['efficiency']::<6.6f}")

if __name__ == '__main__':
    MRMostEfficientPlayers.run()