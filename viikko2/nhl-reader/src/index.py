from player import PlayerReader, PlayerStats, display_players

def main():

    
    while True:
        season = input("Enter the NHL season (2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25): ")
        nationality = input("Enter the nationality code (AUT, CZE, AUS, SWE, GER, DEN, SUI, SVK, NOR, RUS, CAN, LAT, BLR, SLO, USA, FIN, GBR): ").upper()
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        if players:
            display_players(players, nationality, season)
        else:
            print(f"No players found for nationality '{nationality}' in season '{season}'.")

if __name__ == "__main__":
    main()