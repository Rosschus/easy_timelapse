from flask import Flask
import camera_manager
import multiprocessing

app = Flask(__name__)


@app.route('/start', methods=["GET"])
def start_timelapse():
    try:
        processes = multiprocessing.active_children()
        for i in processes:
            if i.name == "river_screening":
                return "Процесс уже запущен", 200
        multiprocessing.Process(target=camera_manager.make_timelaps, name="river_screening").start()
        return "Запуск процесса...", 200
    except Exception as e:
        return e, 500


@app.route('/stop', methods=["GET"])
def stop_timelapse():
    try:
        processes = multiprocessing.active_children()
        for i in processes:
            if i.name == "river_screening":
                i.terminate()
                return "Процесс остановлен", 200
        return "Процесс не запущен", 200
    except Exception as e:
        return e, 500


if __name__ == '__main__':
    multiprocessing.freeze_support()
    app.run()
