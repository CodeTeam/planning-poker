from manager import Manager

from application.app import runserver as run_tornado_server

manager = Manager()


@manager.command
def runserver():
    """Runs tornado server"""
    run_tornado_server()


if __name__ == '__main__':
    manager.main()
