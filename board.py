import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


class Board:
    """
    Kahuna board consists of 12 islands with various bridges between them.
    The current state of the board is represented as a connectivity matrix,
    indicating which bridges are allowed and which are occupied by each player.
    """


    def __init__(self):
        """
        Set up board with no bridges between islands.
        """

        # Set up island ids
        # A=0,B=1,C=2,D=3,E=4,F=5,G=6,H=7,I=8,J=9,K=10,L=11
        self.island_ids = np.arange(12,dtype=int)

        # Set up connectivity matrix
        # This is a 12x12 matrix with indices corresponding to islands Aloa(0) - Lale(11)
        # -1 indicates a disallowed connection, 0 an allowed connection (unoccupied by either player)
        # 1 indicates bridge occupied by player 1, 2 by player 2
        self.state = np.ones((12,12),dtype=int)*-1
        self.state[0,[1,3,7]] = 0
        self.state[1,[0,2,3,4,5]] = 0
        self.state[2,[1,5,6,10]] = 0
        self.state[3,[0,1,4,7]] = 0
        self.state[4,[1,3,5,7,8,9]] = 0
        self.state[5,[1,2,4,6,9]] = 0
        self.state[6,[2,5,9,10]] = 0
        self.state[7,[0,3,4,8,11]] = 0
        self.state[8,[4,7,9,10,11]] = 0
        self.state[9,[4,5,6,8,10]] = 0
        self.state[10,[2,6,8,9,11]] = 0
        self.state[11,[7,8,10]] = 0

        # Set up island coordinates for board visualisation
        self.island_crds = np.zeros((12,2),dtype=float)
        self.island_crds[0,:] = [0.0,10.0]
        self.island_crds[1,:] = [5.0,9.0]
        self.island_crds[2,:] = [9.0,8.0]
        self.island_crds[3,:] = [2.0,7.0]
        self.island_crds[4,:] = [4.0,6.0]
        self.island_crds[5,:] = [7.0,7.0]
        self.island_crds[6,:] = [8.0,6.0]
        self.island_crds[7,:] = [2.0,4.0]
        self.island_crds[8,:] = [5.0,3.0]
        self.island_crds[9,:] = [6.0,4.0]
        self.island_crds[10,:] = [8.0,2.0]
        self.island_crds[11,:] = [5.0,1.0]

        # Set up Matplotlib plot size
        params = {"figure.figsize": (5, 5)}
        pylab.rcParams.update(params)


    def move(self,player,card_a,card_b):
        """
        Move by player with two given cards, which changes board state.
        """



    def display(self):
        """
        Visualise current board state.
        """

        # Set up figure
        fig, ax = plt.subplots()

        # Add island coordinates
        ax.scatter(self.island_crds[:,0],self.island_crds[:,1],s=100,facecolor="w",edgecolor='k',zorder=1)

        # Add bridges
        for i,connections in enumerate(self.state):
            empty_bridges = self.island_ids[connections==0]
            for j in empty_bridges:
                if i<j:
                    ax.plot(self.island_crds[[i,j],0],self.island_crds[[i,j],1],ls='--',c='k',zorder=0)

        # Add island text
        island_names = ["Aloa","Bari","Coco","Duda","Elai","Faaa",
                        "Gola","Huna","Iffi","Jojo","Kahu","Lale"]
        for i,name in enumerate(island_names):
            ax.text(self.island_crds[i,0]-0.5,self.island_crds[i,1]+0.5,name)

        # Set axes properties
        ax.set_xlim(-2,12)
        ax.set_ylim(-2,12)
        ax.set_axis_off()

        # Display
        plt.show()





if __name__ == "__main__":

    board = Board()
    board.display()





