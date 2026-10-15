import psutil


def get_cpu_count():
    # cpu_count повертає кількість ядер процесора
    return psutil.cpu_count()
