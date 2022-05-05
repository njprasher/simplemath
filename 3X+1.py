import matplotlib.pyplot as plt
import numpy as np

class PlotThreeXGraph():
    number=0
    runtime=0
    steps=0
    allGraphData = {runtime:[]}
    arrayofNumber=list(range(0,int(steps)))
    numbersbouncedto=[]

    #plotting the number to line graph
    def makegraph(self):
        if(self.runtime>=1):
            plt.plot(self.arrayofNumber,self.numbersbouncedto, marker = 'o')
        self.number = input('Enter a Number')
        self.numbersbouncedto=[]
        self.steps=0
        x=int(self.number)
        while x!=1:
            if(x%2!=0):
                x=3*x+1
                self.numbersbouncedto.append(int(x))
                self.steps+=1
            else:
                x=x/2
                self.numbersbouncedto.append(int(x))
                self.steps+=1
        
        print('number reduced to ', int(x) ,' : ', int(self.number), 'in', int(self.steps), 'steps')
        print('numbers bounced to ', self.numbersbouncedto)

        #once steps are found we will make an array of 0 to steps
        self.arrayofNumber=list(range(0,int(self.steps)))

        # naming the x axis
        plt.xlabel('Steps Required')
        # naming the y axis
        plt.ylabel('Numbers Bounced to')
        
        # giving a title to my graph
        plt.title('See 3X+1')

        # function to show the plot
        # plotting the points
        plt.plot(self.arrayofNumber,self.numbersbouncedto, marker = 'o')
        #close to render next
        print('PLease close the graph to render next graph')
        # render the plot
        plt.show()

    def askAgain(self):
        userlogic=input('Want to plot another one? (Y/n)')
        while True:        # Loop until it is Y/n
            if userlogic == "Y" or userlogic == "y":
                self.runtime=+1
                self.makegraph()
            elif userlogic == "N" or userlogic == "n":
                quit()
            #Let the user know to enter correct number
            userlogic = input("Is x > y (Y/n) Please use 'Y' or 'n' :")

    def makeGraphTo(self):
        sequence=input('PLease give the number to make graph to?')
        for x in range(1,int(sequence)):
            self.numbersbouncedto=[]
            self.steps=0

            # naming the x axis
            plt.xlabel('Steps Required')
            # naming the y axis
            plt.ylabel('Numbers Bounced to')
            
            # giving a title to my graph
            plt.title('See 3X+1')

            while x!=1:
                if(x%2!=0):
                    x=3*x+1
                    self.numbersbouncedto.append(int(x))
                    self.steps+=1
                else:
                    x=x/2
                    self.numbersbouncedto.append(int(x))
                    self.steps+=1
            
            print('number reduced to ', int(x) ,' : ', int(self.number), 'in', int(self.steps), 'steps')
            print('numbers bounced to ', self.numbersbouncedto)

            #once steps are found we will make an array of 0 to steps
            self.arrayofNumber=list(range(0,int(self.steps)))


            # function to show the plot
            # plotting the points
            plt.plot(self.arrayofNumber,self.numbersbouncedto, marker = ',')
            # render the plot
        plt.show()
        
makeplot = PlotThreeXGraph()
# makeplot.makegraph()
# makeplot.askAgain()

makeplot.makeGraphTo()