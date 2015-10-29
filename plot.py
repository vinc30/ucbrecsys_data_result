from glob import glob
from matplotlib import pyplot as plt
import argparse
from functools import reduce


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--dall", help="Draw graphs for all related files in the folder. --all should be used with other arguments", type=str)
    parser.add_argument(
        "-rgmf", "--regret_mf", help="MF regret data file to be plotted", type=str)
    parser.add_argument(
        "-rwmf", "--reward_mf", help="MF reward data file to be plotted", type=str)
    parser.add_argument("-rgucbmf", "--regret_ucbmf",
                        help="UCBMF regret data file to be plotted", type=str)
    parser.add_argument("-rwucbmf", "--reward_ucbmf",
                        help="UCBMF reward data file to be plotted", type=str)
    parser.add_argument("-rgbewareU", "--regret_bewareU",
                        help="Beware.U regret data file to be plotted", type=str)
    parser.add_argument("-rwbewareU", "--reward_bewareU",
                        help="Beware.U reward data file to be plotted", type=str)
    parser.add_argument("-rgbewareI", "--regret_bewareI",
                        help="Beware.I regret data file to be plotted", type=str)
    parser.add_argument("-rwbewareI", "--reward_bewareI",
                        help="Beware.I reward data file to be plotted", type=str)
    args = parser.parse_args()
    if args.dall:
        if args.regret_mf:
            filepath = glob("./result/*mf_0_regret.dat")

    else:
        if (args.regret_mf):
            regretfile_mf = args.regret_mf
            fp = open(regretfile_mf)
            regret_mf = list(map(lambda x: float(x), fp.readlines()))
            regret_mf_20 = [reduce(
                lambda x, y: x + y, regret_mf[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rg_mf_line = plt.plot(regret_mf_20, label="mf regret")
        if (args.regret_ucbmf):
            regretfile_ucbmf = args.regret_ucbmf
            fp = open(regretfile_ucbmf)
            regret_ucbmf = list(map(lambda x: float(x), fp.readlines()))
            regret_ucbmf_20 = [reduce(
                lambda x, y: x + y, regret_ucbmf[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rg_ucbmf_line = plt.plot(regret_ucbmf_20, label="ucbmf regret")
        if (args.regret_bewareU):
            regretfile_bewareU = args.regret_bewareU
            fp = open(regretfile_bewareU)
            regret_bewareU = list(map(lambda x: float(x), fp.readlines()))
            regret_bewareU_20 = [reduce(
                lambda x, y: x + y, regret_bewareU[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rg_bewareU_line = plt.plot(regret_bewareU_20, label="bewareU regret")
        if (args.regret_bewareI):
            regretfile_bewareI = args.regret_bewareI
            fp = open(regretfile_bewareI)
            regret_bewareI = list(map(lambda x: float(x), fp.readlines()))
            regret_bewareI_20 = [reduce(
                lambda x, y: x + y, regret_bewareI[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rg_bewareI_line = plt.plot(regret_bewareI_20, label="bewareI regret")
        plt.legend()
        plt.show()

        if (args.reward_mf):
            rewardfile_mf = args.reward_mf
            fp = open(rewardfile_mf)
            reward_mf = list(map(lambda x: float(x), fp.readlines()))
            reward_mf_20 = [reduce(
                lambda x, y: x + y, reward_mf[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rw_mf_line = plt.plot(reward_mf_20, label="mf reward")
        if (args.reward_ucbmf):
            rewardfile_ucbmf = args.reward_ucbmf
            fp = open(rewardfile_ucbmf)
            reward_ucbmf = list(map(lambda x: float(x), fp.readlines()))
            reward_ucbmf_20 = [reduce(
                lambda x, y: x + y, reward_ucbmf[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rw_ucbmf_line = plt.plot(reward_ucbmf_20, label="ucbmf reward")
        if (args.reward_bewareU):
            rewardfile_bewareU = args.reward_bewareU
            fp = open(rewardfile_bewareU)
            reward_bewareU = list(map(lambda x: float(x), fp.readlines()))
            reward_bewareU_20 = [reduce(
                lambda x, y: x + y, reward_bewareU[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rw_bewareU_line = plt.plot(reward_bewareU_20, label="bewareU reward")
        if (args.reward_bewareI):
            rewardfile_bewareI = args.reward_bewareI
            fp = open(rewardfile_bewareI)
            reward_bewareI = list(map(lambda x: float(x), fp.readlines()))
            reward_bewareI_20 = [reduce(
                lambda x, y: x + y, reward_bewareI[i:i + 20]) / float(20) for i in range(0, 10000, 20)]
            rw_bewareI_line = plt.plot(reward_bewareI_20, label="bewareI reward")
        plt.legend()
        plt.show()
