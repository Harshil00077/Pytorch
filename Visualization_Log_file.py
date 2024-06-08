import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
model_name = "model_06/08_12:19"


def create_acc_loss_graph(model_name):
    contents = open("model.log","r").read().split('\n')
    acc = []
    loss = []
    val_acc = []
    val_loss = []
    for c in contents:
        if model_name in c:
            m1,t_acc,v_acc,t_loss,v_loss = c.strip().split(',')
            acc.append(float(t_acc[10:]))
            val_acc.append(float(v_acc[8:]))
            loss.append(float(t_loss[12:]))
            val_loss.append(float(v_loss[10:]))
            # print(float(t_acc[10:]),float(v_acc[8:]),float(t_loss[12:]),float(v_loss[10:]))

    # plt.plot(range(len(acc)),acc,label="acc")
    # plt.plot(range(len(acc)),val_acc,label="val_acc")
    # # plt.plot(range(len(loss)),loss)
    # plt.plot(range(len(acc)),loss,label="loss")
    # plt.plot(range(len(acc)),val_loss,label="val_loss")
    # plt.legend()
    # plt.show()
    fig = plt.figure()

    ax1 = plt.subplot2grid((2,1), (0,0))
    ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)


    ax1.plot(range(len(acc)), acc, label="acc")
    ax1.plot(range(len(acc)), val_acc, label="val_acc")
    ax1.legend(loc=2)
    ax2.plot(range(len(acc)),loss, label="loss")
    ax2.plot(range(len(acc)),val_loss, label="val_loss")
    ax2.legend(loc=2)
    plt.show()

    
create_acc_loss_graph(model_name)