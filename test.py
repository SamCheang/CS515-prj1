import subprocess
import os
import sys


def run_test(prog, input_file, expected_output_file):
    with open(input_file, "rb") as f:
        input_data = f.read()

    # Run the program with input as STDIN
    process = subprocess.run(
        ["python", f"{prog}.py"], input=input_data, capture_output=True, text=True
    )
    output = process.stdout

    with open(expected_output_file, "r") as f:
        expected_output = f.read()

    return output == expected_output, output


def main():
    test_dir = "test/"
    test_results = {"OK": 0, "output mismatch": 0, "total": 0}

    for filename in os.listdir(test_dir):
        if filename.endswith(".in"):
            base_name = filename[:-3]
            prog, test_name = base_name.split(".", 1)

            input_file = os.path.join(test_dir, filename)
            output_file = os.path.join(test_dir, base_name + ".out")
            arg_output_file = os.path.join(test_dir, base_name + ".arg.out")

            test_passed, output = run_test(prog, input_file, output_file)
            if not test_passed:
                print(
                    f"FAIL: {prog} {test_name} failed (TestResult.OutputMismatch)\n      expected:\n{output}\n"
                )
                test_results["output mismatch"] += 1
            else:
                test_results["OK"] += 1

            test_results["total"] += 1

    print(
        f"OK: {test_results['OK']}\noutput mismatch: {test_results['output mismatch']}\ntotal: {test_results['total']}"
    )

    if test_results["output mismatch"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
