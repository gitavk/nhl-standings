from dataclasses import dataclass


# Аналитика по музыкальному жанру
@dataclass
class Report:
    # Название музыкального жанра
    genre: str

    # Наиболее популярные значения скоростей (BPM): (количество, значение)
    bpm_chart: list[tuple[int, int]]

    # Наиболее популярные значения тональностей (Key): (количество, значение)
    # Вместо str следует использовать Enum, но это бы усложнило пример
    key_chart: list[tuple[int, str]]
