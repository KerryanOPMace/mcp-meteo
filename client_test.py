# client_test.py
import asyncio
from fastmcp import Client

client=Client("./server.py")

async def main():
    async with client:
        
        
        tools = await client.list_tools()
        print("Outils disponibles:", tools)
        
        # Test météo actuelle par ville
        print("\n>>> Météo Paris")
        result_city = await client.call_tool("get_weather_by_city", {"city": "Paris"})
        print(result_city)

        # Test prévisions par coordonnées
        print("\n>>> Prévisions Paris (coordonnées, 3 jours)")
        result_forecast = await client.call_tool("get_forecast", {
            "latitude": 48.8566,
            "longitude": 2.3522,
            "days": 3
        })
        print(result_forecast)

        # Test prévisions par ville
        print("\n>>> Prévisions Paris (par nom, 5 jours)")
        result_forecast_city = await client.call_tool("get_forecast_by_city", {
            "city": "Paris",
            "days": 5
        })
        print(result_forecast_city)

asyncio.run(main())
