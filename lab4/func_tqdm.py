def progress_bar():
    from tqdm import tqdm
    import time
    for i in tqdm(range(100)):
        time.sleep(0.02)  # імітація роботи
    return "Прогрес-бар завершено!"