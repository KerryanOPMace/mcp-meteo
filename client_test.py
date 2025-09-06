# client_test.py
import asyncio
from fastmcp import Client

client = Client("./mcp_meteo/server.py")

async def main():
    async with client:
        tools = await client.list_tools()
        print("Outils disponibles:", tools)

        # Météo actuelle
        print("\n>>> Météo Paris")
        weather = await client.call_tool("get_weather_by_city", {"city": "Paris"})
        print(weather)

        # Prévisions météo
        print("\n>>> Prévisions Paris (5 jours)")
        forecast = await client.call_tool("get_forecast_by_city", {"city": "Paris", "days": 5})
        print(forecast)

        # Qualité de l’air
        print("\n>>> Qualité de l'air Paris")
        air_quality = await client.call_tool("get_air_quality_by_city", {"city": "Paris"})
        print(air_quality)

        # Marine forecast
        print("\n>>> Prévisions marines Marseille")
        marine = await client.call_tool("get_marine_forecast_by_city", {"city": "Marseille"})
        print(marine)

        # Données historiques
        print("\n>>> Historique météo Paris (2023-01-01 -> 2023-01-07)")
        archive = await client.call_tool("get_archive_weather_by_city", {
            "city": "Paris",
            "start_date": "2023-01-01",
            "end_date": "2023-01-07"
        })
        print(archive)

        # Prévisions saisonnières
        print("\n>>> Prévisions saisonnières Paris")
        seasonal = await client.call_tool("get_seasonal_forecast_by_city", {"city": "Paris"})
        print(seasonal)

        # Prévisions ensemble
        print("\n>>> Prévisions ensemble Paris")
        ensemble = await client.call_tool("get_ensemble_forecast_by_city", {"city": "Paris"})
        print(ensemble)


if __name__ == "__main__":
    asyncio.run(main())
