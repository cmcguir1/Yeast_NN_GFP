from GeneExpressionData import GeneExpressionData
from PredictionModel import PredictionModel
import time

def main():
    start = time.time()
    model = PredictionModel(folder='Dev',modelName='TestModel',numFolds=4,datasetMode='2007')
    model.evaluateFoldPerformance(0)
    print(f'Training took {(time.time() - start)/60} minutes')

if __name__ == "__main__":
    main()