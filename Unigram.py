{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77704b57",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import nltk \n",
    "import string\n",
    "\n",
    "from nltk.util import ngrams\n",
    "\n",
    "from nltk.corpus import udhr  \n",
    "\n",
    "english = udhr.raw('English-Latin1') \n",
    "french = udhr.raw('French_Francais-Latin1') \n",
    "italian = udhr.raw('Italian_Italiano-Latin1') \n",
    "spanish = udhr.raw('Spanish_Espanol-Latin1')  \n",
    "\n",
    "english_train, english_dev = english[0:1000], english[1000:1100]\n",
    "french_train, french_dev = french[0:1000], french[1000:1100]\n",
    "italian_train, italian_dev = italian[0:1000], italian[1000:1100] \n",
    "spanish_train, spanish_dev = spanish[0:1000], spanish[1000:1100] \n",
    "english_test = udhr.words('English-Latin1')[0:1000] \n",
    "french_test = udhr.words('French_Francais-Latin1')[0:1000]\n",
    "italian_test = udhr.words('Italian_Italiano-Latin1')[0:1000] \n",
    "spanish_test = udhr.words('Spanish_Espanol-Latin1')[0:1000]\n",
    "\n",
    "eng_train=list(english_train)\n",
    "#print(eng_train)\n",
    "\n",
    "eng_train = [''.join(c for c in s if c not in string.punctuation) for s in eng_train]\n",
    "\n",
    "#eng_train = [s for s in eng_train if s]\n",
    "\n",
    "eng_train = [s.rstrip() for s in eng_train]\n",
    "\n",
    "eng_train=[item.lower() for item in eng_train]\n",
    "\n",
    "unigrams=eng_train\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "fdist1 = nltk.FreqDist(unigrams)\n",
    "print(fdist1)\n",
    "fdist1\n",
    "print(type(fdist1))\n",
    "eng_test=list(english_test)\n",
    "#print(eng_train)\n",
    "\n",
    "\n",
    "french_training=list(french_train)\n",
    "\n",
    "\n",
    "french_training = [''.join(c for c in s if c not in string.punctuation) for s in french_training]\n",
    "\n",
    "\n",
    "\n",
    "french_training = [s.rstrip() for s in french_training]\n",
    "\n",
    "french_training=[item.lower() for item in french_training]\n",
    "\n",
    "unigrams_french=french_training\n",
    "\n",
    "\n",
    "bigrams_french = list(ngrams(french_training,2))\n",
    "trigrams_french = list(ngrams(french_training,3))\n",
    "\n",
    "\n",
    "\n",
    "fdist3 = nltk.FreqDist(unigrams_french)\n",
    "print(fdist3)\n",
    "fdist3\n",
    "\n",
    "\n",
    "\n",
    "eng_test = [''.join(c for c in s if c not in string.punctuation) for s in eng_test]\n",
    "\n",
    "#eng_train = [s for s in eng_train if s]\n",
    "\n",
    "eng_test = [s.rstrip() for s in eng_test]\n",
    "\n",
    "eng_test=[item.lower() for item in eng_test]\n",
    "\n",
    "eng_test=[item for item in eng_test if not item.isdigit()]\n",
    "\n",
    "listoftestwords=[]\n",
    "\n",
    "\n",
    "\n",
    "n=len(unigrams)\n",
    "\n",
    "for i in eng_test:\n",
    "    prob_eng=1\n",
    "    prob_french=1\n",
    "    for j in i :\n",
    "        ele=i[i.index(j)]\n",
    "\n",
    "    \n",
    "        prob_eng*=fdist1[ele]/n\n",
    "                \n",
    "       \n",
    "        prob_french*=1\n",
    "                      \n",
    "            \n",
    "        prob_french*=fdist3[ele]/n\n",
    "             \n",
    "            \n",
    "                \n",
    "                \n",
    "        \n",
    "           \n",
    "    \n",
    "    if(prob_eng>prob_french):\n",
    "         listoftestwords.append(\"english\")\n",
    "        \n",
    "    else:\n",
    "         listoftestwords.append(\"french\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "fdistaccuracy = nltk.FreqDist(listoftestwords)\n",
    "fdistaccuracy\n",
    "\n",
    "if(fdistaccuracy['english']>fdistaccuracy['french']):\n",
    "    print(\"Tested words is Englisgh as accuracy is more for English\")\n",
    "    accuracy=fdistaccuracy['english']/(fdistaccuracy['french']+fdistaccuracy['english'])\n",
    "    print(accuracy*100)\n",
    "        \n",
    "        \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
