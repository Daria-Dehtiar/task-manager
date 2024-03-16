from tasks.cli import handle_action, handle_interrupt

def main():
    while True:
        try:
            handle_action()
        except KeyboardInterrupt:
            if handle_interrupt():
                break


if __name__ == '__main__':
    main()