def map_reduce(file_path,target_word):
    word_count=0
    char_count=0
    with open(file_path,'r') as file:
        mapped_data=[(word.lower(),1) for line in file for word in line.strip().split()]
        file.seek(0)
        char_count=sum(len(line) for line in file)
        
    
    for word,count in mapped_data:
        if word==target_word.lower():
            word_count+=count
    return word_count,char_count
file_path='test.txt'
target_word='start'
frequency,total_chars=map_reduce(file_path,target_word)
print(f"The word {target_word} appears {frequency} times")
print(f"The character count is {total_chars}")

####Sentence count code####

def map_reduce(file_path, target_word):
    word_count = 0
    char_count = 0
    sentence_count = 0

    with open(file_path, 'r') as file:
        # Count words (map phase)
        mapped_data = [(word.lower(), 1) for line in file for word in line.strip().split()]
        
        # Reset file pointer to read again
        file.seek(0)
        
        # Count characters and sentences
        for line in file:
            char_count += len(line)
            sentence_count += line.count('.') + line.count('!') + line.count('?')

    # Count occurrences of the target word (reduce phase)
    for word, count in mapped_data:
        if word == target_word.lower():
            word_count += count

    return word_count, char_count, sentence_count

# Example usage
file_path = 'test.txt'
target_word = 'start'
frequency, total_chars, total_sentences = map_reduce(file_path, target_word)

print(f"The word '{target_word}' appears {frequency} times.")
print(f"The character count is {total_chars}.")
print(f"The number of sentences is {total_sentences}.")


#####Unique words#####

def map_reduce(file_path, target_word):
    word_count = 0
    char_count = 0
    unique_words = set()

    with open(file_path, 'r') as file:
        mapped_data = []
        for line in file:
            words = line.strip().split()
            for word in words:
                word_lower = word.lower()
                mapped_data.append((word_lower, 1))
                unique_words.add(word_lower)
        
        # Reset file pointer and calculate character count
        file.seek(0)
        char_count = sum(len(line) for line in file)

    # Count the occurrences of the target word
    for word, count in mapped_data:
        if word == target_word.lower():
            word_count += count

    return word_count, char_count, len(unique_words)

# Example usage
file_path = 'test.txt'
target_word = 'start'
frequency, total_chars, unique_word_count = map_reduce(file_path, target_word)

print(f"The word '{target_word}' appears {frequency} times.")
print(f"The character count is {total_chars}.")
print(f"The number of unique words is {unique_word_count}.")


####weather code#####


def map_reduce(file_path):
    with open(file_path,'r') as file:
        mapped=[line.strip().split(',') for line in file]
        mapped=[(int(year),int(temp)) for year,temp in mapped]
    coolest_year=min(mapped,key=lambda x:x[1])
    hottest_year=max(mapped,key=lambda x:x[1])
    return coolest_year,hottest_year
file_path='9th ass.txt'
coolest,hottest=map_reduce(file_path)

print(f"The coolest year {coolest[0]} with temperature {coolest[1]}")