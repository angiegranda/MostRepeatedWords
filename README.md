# MostRepeatedWords
Small Task : Input in the console a text, use a hash table to answer queries about word frequencies


**Build a hash table mapping each word in the input to its number of occurrences. For this assignment, a word is any sequence of lowercase or uppercase characters from the Latin alphabet, i.e. the letters 'a'...'z' or 'A'...'Z'. You should ignore case: "pizza" and "Pizza" are the same word.**

**After you read the line '== END ==', write the number of unique words in the input text (i.e. the number of entries in your hash table) on an output.**

**Now a series of queries will follow, one per line. Each query is a single word. Write the word and its number of occurrences in the input text, separated by a single space. If the word is not present in the text, write None in place of a number.**

**If there are multiple queries for the same word, you should report a number of occurrences for the first query only. For all subsequent queries, write None. (To accomplish this, remove a word from the hash table after it has been queried.)**

**Sample input:**

#### I met a traveller from an antique land
#### Who said: "Two vast and trunkless legs of stone
#### Stand in the desert. Near them on the sand,
#### Half sunk, a shattered visage lies, whose frown
#### And wrinkled lip and sneer of cold command
#### Tell that its sculptor well those passions read
#### Which yet survive, stamped on these lifeless things,
#### The hand that mocked them and the heart that fed.
#### And on the pedestal these words appear:
#### `My name is Ozymandias, King of Kings:
#### Look on my works, ye mighty, and despair!'
#### Nothing beside remains. Round the decay
#### Of that colossal wreck, boundless and bare,
#### The lone and level sands stretch far away".
#### == END ==
#### and
#### vast
#### boundless
#### sky
#### these
#### sand
#### and
#### sand

#### Output: 

#### resizing to 10 buckets
#### resizing to 20 buckets
#### resizing to 40 buckets
#### unique words = 85
#### and 8
#### vast 1
#### boundless 1
#### sky None
#### these 2
#### sand 1
#### and None
#### sand None

#### Sample input #2:

#### Ho, Giant! This is I!
#### I have built me a bean-stalk into your sky!
#### La,--but it's lovely, up so high!
#### == END ==
#### bean
#### stalk
#### giant
#### la
#### lovely
#### cloud
#### sky
#### sky

#### Output:

#### resizing to 10 buckets
#### unique words = 22
#### bean 1
#### stalk 1
#### giant 1
#### la 1
#### lovely 1
#### cloud None
#### sky 1
#### sky None

#### Sample input #3:

#### tree tree tree tree tree tree tree tree tree tree
#### tree tree tree tree tree tree tree tree tree tree
#### tree tree tree tree tree tree tree tree tree tree
#### tree tree tree tree tree tree tree tree tree tree
#### == END ==
#### tree
#### Output:

#### unique words = 1
#### tree 40
#### Sample input #5:
