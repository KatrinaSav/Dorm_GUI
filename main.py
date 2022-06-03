import cli
from view.View import DormApp


def main(interface_type):
    if interface_type.lower() == 'gui':
        DormApp().run()
    elif interface_type.lower() == 'cli':
        cli.run()
    else:
        print('Unavailable format.')
        exit()


if __name__ == '__main__':
    print('Выберите режим запуска: GUI или CLI')
    mode = input()
    main(mode)


