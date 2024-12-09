

def calculate_dive_score(line):
    #cal single dive
    parts = line.strip().split("\t")

    #parse
    diver_name = parts[0]
    degree_of_difficulty = float(parts[1])
    scores = list(map(float, parts[2:]))

    #remove the highest and lowest scores
    scores.remove(max(scores))
    scores.remove(min(scores))

    #calculate the average of the remaining s
    aver_score = sum(scores) / len(scores)

    #final score
    final_score= aver_score * degree_of_difficulty

    return diver_name, degree_of_difficulty, round(final_score,1)


def process_file(file_path):
    #read input file
    with open ('input.txt','r') as file:
        lines = file.readlines()
    #print headers
    print(f"{'Name':<15}{'DD':<5}{'Score':<5}")

    for line in lines:
        try:
            diver_name, dd, final_score = calculate_dive_score(line)
            print(f"{diver_name:<15}{dd:<5.1f}{final_score:<5.1f}")
        except Exception as e:
            print(f"Error processing line: {line.strip()} - {e}")

#main
if __name__ ==  "__main__":
    input_file = "input.txt"
    process_file(input_file)