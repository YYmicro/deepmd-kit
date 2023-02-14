import os
now_dir = os.getcwd()
files = os.listdir(now_dir)
results = []
for i in files:
    if os.path.splitext(i)[-1] == '.txt':
        # print(i)
        # print(os.path.splitext(i)[0])
        numbers = os.path.splitext(i)[0].split("_")
        omp = int(numbers[0])
        intra = int(numbers[1])
        inter = int(numbers[2])
        # print(i, j, k)
        with open(i, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # print(i, lines[-1])
        try:
            time = float(lines[-1][98:105])
            # print(time)
            result = [time, omp, intra, inter]
            results.append(result)
            # break
        except ValueError:
            print(f'file {i} is uncomplished')

print(results)
results = sorted(results, key=lambda result:result[0])
for result in results:
    print(result)
        


