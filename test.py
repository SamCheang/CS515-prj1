import os
import subprocess
import sys

def run_test(prog, input_path, expected_output, arg_mode=False):
    with open(input_path, 'r') as file:
        input_data = file.read()

    if arg_mode:
        process = subprocess.run(['python', f'prog/{prog}.py', input_path], capture_output=True, text=True)
    else:
        process = subprocess.run(['python', f'prog/{prog}.py'], input=input_data, capture_output=True, text=True)

    return process.stdout == expected_output, process.stdout

def main():
    test_directory = 'test/'
    tests_passed = 0
    total_tests = 0

    for filename in os.listdir(test_directory):
        if filename.endswith('.in'):
            prog, test_name = filename[:-3].split('.')
            with open(f'{test_directory}/{prog}.{test_name}.out', 'r') as file:
                expected_output = file.read()

            # Test using STDIN
            result, output = run_test(prog, f'{test_directory}/{filename}', expected_output)
            if result:
                tests_passed += 1
            else:
                print(f'FAIL: {prog} {test_name} failed (TestResult.OutputMismatch)')
                print('      expected:')
                print(expected_output)
                print('\n           got:')
                print(output)

            # Test using command line argument
            arg_out_path = f'{test_directory}/{prog}.{test_name}.arg.out'
            if os.path.exists(arg_out_path):
                with open(arg_out_path, 'r') as file:
                    expected_arg_output = file.read()

                result, output = run_test(prog, f'{test_directory}/{filename}', expected_arg_output, arg_mode=True)
                if result:
                    tests_passed += 1
                else:
                    print(f'FAIL: {prog} {test_name} failed in argument mode (TestResult.OutputMismatch)')
                    print('      expected:')
                    print(expected_arg_output)
                    print('\n           got:')
                    print(output)

            total_tests += 2

    print(f'\nOK: {tests_passed}')
    print(f'output mismatch: {total_tests - tests_passed}')
    print(f'total: {total_tests}')

    if tests_passed != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()
