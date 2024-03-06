from openai_api import OpenAIAPI

def exit_program(gpt_api: OpenAIAPI) -> None:
    exit()

def set_custom(gpt_api: OpenAIAPI) -> None:
    custom_instruction = input('Enter custom instruction > ')
    gpt_api.set_custom_instruction(custom_instruction)

COMMANDS = {
    'exit': exit_program,
    'setcustom': set_custom
}

def main():
    gpt_api = OpenAIAPI()
    while True:
        user_input = input('> ')

        # handle commands
        if user_input[:1] == '/':
            command = user_input[1:]
            if command not in COMMANDS:
                print('Invalid command!')
            else:
                COMMANDS[command](gpt_api)
            continue

        response = gpt_api.get_response(user_input)
        print(f'gpt-3.5-turbo: {response}')

if __name__ == '__main__':
    main()