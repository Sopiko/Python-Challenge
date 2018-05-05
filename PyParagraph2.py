def paragraphAnalysis(filename):
    letterCount = 0
    paragraphNumber = 1
    with open('raw_data\\' + filename, newline='', encoding='utf-8') as paragraph:
        
        # Import a text file filled with a paragraph of our choosing
        for textBlock in paragraph:
            # Assess the passage for each of the following:
            if len(textBlock) != 1: # eliminate blank paragraphs
                # Approximate word count
                wordCount = textBlock.split(' ')

                # Approximate sentence count
                sentenceCount = re.split('[.!?]+', textBlock)
                # The above adds an empty bit at the end  and needs to be removed
                sentenceCount.pop(-1)

                # Approximate letter count (per word)
                for word in wordCount:
                    letterCount = letterCount + len(word)
                letterCount = letterCount / len(wordCount)
                
                # Average sentence length (in word)
                for sentence in sentenceCount:
                    swordCount = sentence.split(' ')
                    swordCount = len(swordCount)
                swordCount = swordCount / len(sentenceCount)

                #OUTPUT
                print(filename)
                print('Paragraph #' + str(paragraphNumber) + ' Analysis')
                print('-----------------')
                print('Approximate Word Count: ' + str(len(wordCount)))
                print('Approximate Sentence Count: ' + str(len(sentenceCount)))
                print('Average Letter Count: ' + str(letterCount))
                print('Average Sentence Length: ' + str(swordCount) + '\n')
                paragraphNumber = paragraphNumber + 1

paragraphAnalysis('paragraph_1.txt')
paragraphAnalysis('paragraph_2.txt')