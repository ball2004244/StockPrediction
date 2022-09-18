import matplotlib.pyplot as plt 

def graph(lst_x, lst_y, _label):
    plt.plot(lst_x, lst_y, label=str(_label))

def vertical_line(_x):
    ax = plt.gca()
    ax.axvline(x=_x, color='b')

def horizontal_line(_y):
    ax = plt.gca()
    ax.axhline(y=_y, color='b')

def setup_graph():
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('Just A Graph')
    plt.legend()

    ax = plt.gca()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    ax.set_xlim([-3, 5])
    ax.set_ylim([-3, 6])

    plt.show()