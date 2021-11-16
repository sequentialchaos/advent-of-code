import csv


def main():
    d = make_dict()
    table = make_table(d)
    readme_str = read_readme() + table
    write_to_readme(readme_str)


def read_readme():
    readme_str = ''
    with open('README.md', 'r') as f:
        for line in f.readlines():
            if 'day ↓ year →' in line:
                break
            readme_str += line
    return readme_str


def write_to_readme(readme_str):
    with open('README.md', 'w') as f:
        f.write(readme_str)


def make_table(d):
    table = ''
    table += '|day ↓ year → |'
    for year in range(2015, 2020+1):
        table += str(year) + '|'
    table += '\n|:--------------:|'
    for year in range(2015, 2020+1):
        table += ':-------:|'
    table += '\n'
    for day in range(1, 25+1):
        day_str = str(day)
        table += f'|{day}|'
        for year in range(2015, 2020+1):
            year_str = str(year)
            if year_str in d:
                if day_str in d[year_str]:
                    languages = d[year_str][day_str]['languages']
                    urls = d[year_str][day_str]['urls']
                    for i in range(len(languages)):
                        table += f'[{languages[i]}]({urls[i]})'
                        if i < len(languages) - 1:
                            table += ','
            table += '|'
        table += '\n'
    return table


def make_dict():
    d = {}
    base_url = 'https://www.github.com/sequentialchaos/advent-of-code/tree/master/'
    with open('completed.tsv') as tsv_completed:
        csv_reader = csv.reader(tsv_completed, delimiter='\t')
        line_count = 0
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            print(row)
            year, day, languages = row[0], row[1], row[2].split(',')
            d.setdefault(year, {})
            d[year][day] = {}
            d[year][day]['languages'] = languages
            urls = []
            for language in languages:
                urls.append(f'{base_url}{year}/{language}/' +
                            url_end(language, day))
            d[year][day]['urls'] = urls
    return d


def url_end(language, day):
    if language == 'javascript':
        return f'day{day.zfill(2)}/solution.js'
    elif language == 'python':
        return f'day{day.zfill(2)}.py'
    elif language == 'haskell':
        return f'Day{day.zfill(2)}.hs'


if __name__ == '__main__':
    main()
