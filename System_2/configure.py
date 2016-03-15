FILE_LINE_SENTANCE='./data/2016_aicyber_wiki_weibo_douban_words_l5.txt'
W2V_OUTPUT_MODEL='./data/w2v/w2v_wiki_weibo_douban_20.bin'
TRAIN_SET='./data/douban_c5.train.txt'
EVAL_SET='./data/douban_c5.eval.txt'
IMDB_BOW_DATA_FOLD= './imdb'
KAGLE_FILE_TEST='./imdb/testData.tsv'
KAGLE_FILE_TEST_LINE_SENTANCE='./tempfolder/imdb_test_line_sentance'
KAGLE_FILE_ALL_LINE_SENTANCE='./tempfolder/imdb_all_train_unlabled_line_sentance'
KAGLE_FILE_TRAIN_W2V_LINE_SENTANCE= './tempfolder/imdb_train_line_sentance'
KAGLE_FILE_TRAIN_IVECTOR_LINE_SENTANCE=KAGLE_FILE_ALL_LINE_SENTANCE
KAGLE_W2V_MODEL='./tempfolder/imdb_trained_75000.w2v.20.bin'
SEMEVAL_TRAIN='../semeval2016/100_topics_100_tweets.sentence-three-point.subtask-A.train.gold.txt.full'
SEMEVAL_DEV='../semeval2016/100_topics_100_tweets.sentence-three-point.subtask-A.dev.gold.txt.full'
SEMEVAL_DEV_TEST='../semeval2016/100_topics_100_tweets.sentence-three-point.subtask-A.devtest.gold.txt.full'
SEMEVAL_TRAIN_FILE_LINE_SENTANCE='./tempfolder/semeval.train.2016.txt'
SEMEVAL_DEV_FILE_LINE_SENTANCE='./tempfolder/semeval.dev,2016.txt'
SEMEVAL_DEV_TEST_FILE_LINE_SENTANCE='./tempfolder/semeval.dev.test.2016.txt'
#TWEET_STANDFORD_FILE_LINE_SENTANCE='./downloads/trainAndUnalbed_stand_ford'

#Output of 0020_...
KALDI_DATA_IMDB_TRAIN='./data/imdb_train'
KALDI_DATA_IMDB_TEST='./data/imdb_test'
KALDI_DATA_SEMEVAL_TRAIN='./data/semeval_train'
KALDI_DATA_SEMEVAL_DEV='./data/semeval_dev'
KALDI_DATA_SEMEVAL_DEVTEST='./data/semeval_devtest'




SCORE_SCRIPT='../semeval2016/score-semeval2016-task4-subtaskA.pl'
SCORE_REF_DEV='../semeval2016/100_topics_100_tweets.sentence-three-point.subtask-A.dev.gold.txt.full'
SCORE_REF_DEVTEST='../semeval2016/100_topics_100_tweets.sentence-three-point.subtask-A.devtest.gold.txt.full'


def loadFeatsText(fname):
    rvvalues=[]
    fdata=open(fname).read()
    fdata=fdata.replace('[\n','[').replace('[ \n','[')
    fdata=fdata.split('\n')
    fdata=[s.replace('[','').replace(']','').replace('  ',' ').replace('  ',' ').strip() for s in fdata if len(s)>10 and '_22 ' not in s ]
    print fdata[0]
    rvids=[s.split()[0] for s in fdata]
    values=[map(float,s.split()[1:]) for s in fdata]
    return rvids,values



