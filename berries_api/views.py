import statistics

import plotly.graph_objs as go
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from plotly.io import to_html


def all_berry_stats(request):
    url = f"{settings.POKEMON_API_URL}berry/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        berries = data.get("results", [])
        growth_times = [int(requests.get(berry["url"]).json()["growth_time"]) for berry in berries]
        min_growth_time = min(growth_times)
        median_growth_time = statistics.median(growth_times)
        max_growth_time = max(growth_times)
        variance_growth_time = statistics.variance(growth_times)
        mean_growth_time = statistics.mean(growth_times)
        frequency_growth_time = {time: growth_times.count(time) for time in set(growth_times)}

        # Crear un histograma con Plotly
        histogram = go.Figure(data=[go.Histogram(x=growth_times)])
        histogram.update_layout(
            title="Distribución de tiempos de crecimiento de bayas",
            xaxis_title="Tiempo de crecimiento",
            yaxis_title="Frecuencia",
            bargap=0.1,
        )

        # Convertir el gráfico a HTML
        histogram_html = to_html(histogram, full_html=False)

        return render(
            request,
            "berries_api/berry_stats.html",
            {
                "berries_names": [berry["name"] for berry in berries],
                "min_growth_time": min_growth_time,
                "median_growth_time": median_growth_time,
                "max_growth_time": max_growth_time,
                "variance_growth_time": variance_growth_time,
                "mean_growth_time": mean_growth_time,
                "frequency_growth_time": frequency_growth_time,
                "histogram_html": histogram_html,
            },
        )
    else:
        return JsonResponse({"error": "Failed to fetch data from PokeAPI"}, status=500)
