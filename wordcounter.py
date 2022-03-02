import sys
import re

def main():
    counter = {}

    try:
        if not len(sys.argv) == 2:
            raise TypeError
        with open(sys.argv[1], 'r') as input:
            words = ' '.join(re.findall('[a-zA-Z]+', input.read())).lower().split()
            for word in words:
                if word not in counter:
                    counter[word] = 1
                else:
                    counter[word] += 1
            sorted_counter = {k: v for k, v in sorted(counter.items(), reverse=True, key=lambda item: item[1])}
    except (TypeError, IndexError, FileNotFoundError):
        print('Error: Invalid execution.')
        sys.exit()

    with open(f'{sys.argv[1].split(".")[0]}-counter.txt', 'w') as output:
        output.write(f'Total words: {len(words)}\n')
        output.write(f'Unique words: {len(set(words))}\n\n')
        for word in sorted_counter.keys():
            output.write(f'{word:8} - {sorted_counter[word]:8}\n')


if __name__ == '__main__':
    main()
    