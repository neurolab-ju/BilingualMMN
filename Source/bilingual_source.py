"""
BILINGUAL MISMATCH NEGATIVITY SOURCE TABLE

Created on Sat Jun  3 11:48:23 2017
@Author: Michael Tesař
@Email: <tesarm@jcu.cz>
University of South Bohemia

Generates a source table for Bilingual MMN
paradigm. All is based on several papers from:

Szychowska, M. (Ed.). (2016). Effects of sound pressure 
level and visual perceptual load on the auditory mismatch 
negativity. Neuroscience letters, 640(2017), 37-41.
https://goo.gl/640Qha

Wiens, S. (Ed.). (2017). Data on the auditory duration 
mismatch negativity for different sound pressure levels 
and visual perceptual loads. Data in brief, 11(2017), 159-164.
https://goo.gl/Whunl9
"""
import random
import pandas

sequence = [3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 
            5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 
            6, 6, 6, 7, 7]
letters = ["H", "K", "M", "N", "V", "W", "Z"]


def buildsequence(sequence, complexity):
    block = list()
    """
    Generate small 125 block with different 
    complexity
    Input:
        complexity (Int) 0 - low complexity, 1 - high complexity
    Output:
        block (list) - full factor matrix
    """
    if complexity == 0:
        # All 6 Xs
        complexity_label = "low complexity"
    else:
        # Just one X
        complexity_label = "high complexity"
        
    random.shuffle(sequence)
    for trial in sequence:
        for sub_trial in range(trial):
            random.shuffle(letters)
            sub_letters = letters[0:6]
            # Deviant
            if sub_trial == 0:
                # Low complexity
                if complexity == 0:
                    sub_letters = ["X", "X", "X", "X", "X", "X"]
                # High complexity
                else:   
                    x_index = random.randint(0, 5)
                    sub_letters[x_index] = "X"
                    
                sub_letters.append("deviant")
                sub_letters.append(complexity_label)
                block.append(sub_letters)
            # Standard    
            else:
                sub_letters.append("standard")
                sub_letters.append(complexity_label)
                block.append(sub_letters)
    return block


def buildblock():
    """
    Build block of 250 trials consists of two
    125 trials sequences of two different
    complexity.
    """
    source_data = buildsequence(sequence, 1)
    
    return source_data

    
def writeblock(final_block):
    """
    For saving it has to be transformed to 
    DataFrame structure with Pandas library. 
    Also header is included.
    """
    block_df = pandas.DataFrame(final_block, columns = ["Letter1", "Letter2",
                                                        "Letter3", "Letter4",
                                                        "Letter5", "Letter6",
                                                        "Type", "Complexity"])
    block_df.to_csv("Source2.csv", index=False, header=True)    
    
                
if __name__ == "__main__":
    source = []
    for block in range(10):
        final_block = buildblock()
        source.extend(final_block)
        
    writeblock(source)