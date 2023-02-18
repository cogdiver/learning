from typing import Dict, List

def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
        merged = first
        for key in second:
            if key in merged:
                merged[key] = merged[key] + second[key]
            else:
                merged[key] = second[key]
        return merged

def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, _, count = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter

