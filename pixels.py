import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class PixelReader:
    def __init__(self, mask=None):
        self._array_info = 'data/ar3.txt'
        self._pixel_dict = {
            '1': {'f150': [97, 161], 'f90': [1, 960]},
            '10': {'f150': [42, 106], 'f90': [10, 969]},
            '11': {'f150': [43, 107], 'f90': [11, 970]},
            '13': {'f150': [109, 173], 'f90': [13, 972]},
            '131': {'f150': [227, 291], 'f90': [131, 195]},
            '14': {'f150': [110, 174], 'f90': [14, 973]},
            '143': {'f150': [239, 303], 'f90': [143, 207]},
            '147': {'f150': [243, 307], 'f90': [147, 211]},
            '15': {'f150': [111, 175], 'f90': [15, 974]},
            '152': {'f150': [184, 248], 'f90': [152, 216]},
            '153': {'f150': [185, 249], 'f90': [153, 217]},
            '154': {'f150': [186, 250], 'f90': [154, 218]},
            '155': {'f150': [187, 251], 'f90': [155, 219]},
            '156': {'f150': [188, 252], 'f90': [156, 220]},
            '157': {'f150': [189, 253], 'f90': [157, 221]},
            '158': {'f150': [190, 254], 'f90': [158, 222]},
            '159': {'f150': [191, 255], 'f90': [159, 223]},
            '17': {'f150': [113, 177], 'f90': [17, 976]},
            '18': {'f150': [114, 178], 'f90': [18, 977]},
            '19': {'f150': [115, 179], 'f90': [19, 978]},
            '192': {'f150': [352, 416], 'f90': [192, 256]},
            '193': {'f150': [353, 417], 'f90': [193, 257]},
            '194': {'f150': [354, 418], 'f90': [194, 258]},
            '196': {'f150': [228, 292], 'f90': [196, 260]},
            '197': {'f150': [293, 357], 'f90': [197, 261]},
            '198': {'f150': [294, 358], 'f90': [198, 262]},
            '199': {'f150': [295, 359], 'f90': [199, 263]},
            '2': {'f150': [98, 162], 'f90': [2, 961]},
            '200': {'f150': [232, 296], 'f90': [200, 264]},
            '201': {'f150': [297, 361], 'f90': [201, 265]},
            '202': {'f150': [298, 362], 'f90': [202, 266]},
            '203': {'f150': [299, 363], 'f90': [203, 267]},
            '204': {'f150': [364, 428], 'f90': [204, 268]},
            '205': {'f150': [365, 429], 'f90': [205, 269]},
            '206': {'f150': [366, 430], 'f90': [206, 270]},
            '208': {'f150': [368, 432], 'f90': [208, 272]},
            '209': {'f150': [369, 433], 'f90': [209, 273]},
            '21': {'f150': [53, 117], 'f90': [21, 980]},
            '210': {'f150': [370, 434], 'f90': [210, 274]},
            '212': {'f150': [244, 308], 'f90': [212, 276]},
            '213': {'f150': [309, 373], 'f90': [213, 277]},
            '214': {'f150': [310, 374], 'f90': [214, 278]},
            '215': {'f150': [311, 375], 'f90': [215, 279]},
            '22': {'f150': [54, 118], 'f90': [22, 981]},
            '23': {'f150': [55, 119], 'f90': [23, 982]},
            '24': {'f150': [56, 120], 'f90': [24, 88]},
            '25': {'f150': [57, 121], 'f90': [25, 89]},
            '259': {'f150': [355, 419], 'f90': [259, 323]},
            '26': {'f150': [58, 122], 'f90': [26, 90]},
            '27': {'f150': [59, 123], 'f90': [27, 91]},
            '271': {'f150': [367, 431], 'f90': [271, 335]},
            '275': {'f150': [371, 435], 'f90': [275, 339]},
            '28': {'f150': [60, 124], 'f90': [28, 92]},
            '280': {'f150': [312, 376], 'f90': [280, 344]},
            '281': {'f150': [313, 377], 'f90': [281, 345]},
            '282': {'f150': [314, 378], 'f90': [282, 346]},
            '283': {'f150': [315, 379], 'f90': [283, 347]},
            '284': {'f150': [316, 380], 'f90': [284, 348]},
            '285': {'f150': [317, 381], 'f90': [285, 349]},
            '286': {'f150': [318, 382], 'f90': [286, 350]},
            '287': {'f150': [319, 383], 'f90': [287, 351]},
            '29': {'f150': [61, 125], 'f90': [29, 93]},
            '3': {'f150': [99, 163], 'f90': [3, 962]},
            '30': {'f150': [62, 126], 'f90': [30, 94]},
            '31': {'f150': [63, 127], 'f90': [31, 95]},
            '320': {'f150': [480, 544], 'f90': [320, 384]},
            '321': {'f150': [481, 545], 'f90': [321, 385]},
            '322': {'f150': [482, 546], 'f90': [322, 386]},
            '324': {'f150': [356, 420], 'f90': [324, 388]},
            '325': {'f150': [421, 485], 'f90': [325, 389]},
            '326': {'f150': [422, 486], 'f90': [326, 390]},
            '327': {'f150': [423, 487], 'f90': [327, 391]},
            '328': {'f150': [360, 424], 'f90': [328, 392]},
            '329': {'f150': [425, 489], 'f90': [329, 393]},
            '33': {'f150': [33, 992], 'f90': [832, 896]},
            '330': {'f150': [426, 490], 'f90': [330, 394]},
            '331': {'f150': [427, 491], 'f90': [331, 395]},
            '332': {'f150': [492, 556], 'f90': [332, 396]},
            '333': {'f150': [493, 557], 'f90': [333, 397]},
            '334': {'f150': [494, 558], 'f90': [334, 398]},
            '336': {'f150': [496, 560], 'f90': [336, 400]},
            '337': {'f150': [497, 561], 'f90': [337, 401]},
            '338': {'f150': [498, 562], 'f90': [338, 402]},
            '34': {'f150': [34, 993], 'f90': [833, 897]},
            '340': {'f150': [372, 436], 'f90': [340, 404]},
            '341': {'f150': [437, 501], 'f90': [341, 405]},
            '342': {'f150': [438, 502], 'f90': [342, 406]},
            '343': {'f150': [439, 503], 'f90': [343, 407]},
            '35': {'f150': [35, 994], 'f90': [834, 898]},
            '387': {'f150': [483, 547], 'f90': [387, 451]},
            '399': {'f150': [495, 559], 'f90': [399, 463]},
            '403': {'f150': [499, 563], 'f90': [403, 467]},
            '408': {'f150': [440, 504], 'f90': [408, 472]},
            '409': {'f150': [441, 505], 'f90': [409, 473]},
            '410': {'f150': [442, 506], 'f90': [410, 474]},
            '411': {'f150': [443, 507], 'f90': [411, 475]},
            '412': {'f150': [444, 508], 'f90': [412, 476]},
            '413': {'f150': [445, 509], 'f90': [413, 477]},
            '414': {'f150': [446, 510], 'f90': [414, 478]},
            '415': {'f150': [447, 511], 'f90': [415, 479]},
            '448': {'f150': [608, 672], 'f90': [448, 512]},
            '449': {'f150': [609, 673], 'f90': [449, 513]},
            '45': {'f150': [45, 1004], 'f90': [844, 908]},
            '450': {'f150': [610, 674], 'f90': [450, 514]},
            '452': {'f150': [484, 548], 'f90': [452, 516]},
            '453': {'f150': [549, 613], 'f90': [453, 517]},
            '454': {'f150': [550, 614], 'f90': [454, 518]},
            '456': {'f150': [488, 552], 'f90': [456, 520]},
            '457': {'f150': [553, 617], 'f90': [457, 521]},
            '458': {'f150': [554, 618], 'f90': [458, 522]},
            '46': {'f150': [46, 1005], 'f90': [845, 909]},
            '460': {'f150': [620, 684], 'f90': [460, 524]},
            '461': {'f150': [621, 685], 'f90': [461, 525]},
            '462': {'f150': [622, 686], 'f90': [462, 526]},
            '464': {'f150': [624, 688], 'f90': [464, 528]},
            '465': {'f150': [625, 689], 'f90': [465, 529]},
            '466': {'f150': [626, 690], 'f90': [466, 530]},
            '468': {'f150': [500, 564], 'f90': [468, 532]},
            '469': {'f150': [565, 629], 'f90': [469, 533]},
            '47': {'f150': [47, 1006], 'f90': [846, 910]},
            '470': {'f150': [566, 630], 'f90': [470, 534]},
            '49': {'f150': [49, 1008], 'f90': [848, 912]},
            '5': {'f150': [37, 101], 'f90': [5, 964]},
            '50': {'f150': [50, 1009], 'f90': [849, 913]},
            '51': {'f150': [51, 1010], 'f90': [850, 914]},
            '515': {'f150': [611, 675], 'f90': [515, 579]},
            '519': {'f150': [551, 615], 'f90': [519, 583]},
            '523': {'f150': [555, 619], 'f90': [523, 587]},
            '527': {'f150': [623, 687], 'f90': [527, 591]},
            '531': {'f150': [627, 691], 'f90': [531, 595]},
            '535': {'f150': [567, 631], 'f90': [535, 599]},
            '536': {'f150': [568, 632], 'f90': [536, 600]},
            '537': {'f150': [569, 633], 'f90': [537, 601]},
            '538': {'f150': [570, 634], 'f90': [538, 602]},
            '539': {'f150': [571, 635], 'f90': [539, 603]},
            '540': {'f150': [572, 636], 'f90': [540, 604]},
            '541': {'f150': [573, 637], 'f90': [541, 605]},
            '542': {'f150': [574, 638], 'f90': [542, 606]},
            '543': {'f150': [575, 639], 'f90': [543, 607]},
            '576': {'f150': [736, 800], 'f90': [576, 640]},
            '577': {'f150': [737, 801], 'f90': [577, 641]},
            '578': {'f150': [738, 802], 'f90': [578, 642]},
            '580': {'f150': [612, 676], 'f90': [580, 644]},
            '581': {'f150': [677, 741], 'f90': [581, 645]},
            '582': {'f150': [678, 742], 'f90': [582, 646]},
            '584': {'f150': [616, 680], 'f90': [584, 648]},
            '585': {'f150': [681, 745], 'f90': [585, 649]},
            '586': {'f150': [682, 746], 'f90': [586, 650]},
            '588': {'f150': [748, 812], 'f90': [588, 652]},
            '589': {'f150': [749, 813], 'f90': [589, 653]},
            '590': {'f150': [750, 814], 'f90': [590, 654]},
            '592': {'f150': [752, 816], 'f90': [592, 656]},
            '593': {'f150': [753, 817], 'f90': [593, 657]},
            '594': {'f150': [754, 818], 'f90': [594, 658]},
            '596': {'f150': [628, 692], 'f90': [596, 660]},
            '597': {'f150': [693, 757], 'f90': [597, 661]},
            '598': {'f150': [694, 758], 'f90': [598, 662]},
            '6': {'f150': [38, 102], 'f90': [6, 965]},
            '64': {'f150': [224, 288], 'f90': [64, 128]},
            '643': {'f150': [739, 803], 'f90': [643, 707]},
            '647': {'f150': [679, 743], 'f90': [647, 711]},
            '65': {'f150': [225, 289], 'f90': [65, 129]},
            '651': {'f150': [683, 747], 'f90': [651, 715]},
            '655': {'f150': [751, 815], 'f90': [655, 719]},
            '659': {'f150': [755, 819], 'f90': [659, 723]},
            '66': {'f150': [226, 290], 'f90': [66, 130]},
            '663': {'f150': [695, 759], 'f90': [663, 727]},
            '664': {'f150': [696, 760], 'f90': [664, 728]},
            '665': {'f150': [697, 761], 'f90': [665, 729]},
            '666': {'f150': [698, 762], 'f90': [666, 730]},
            '667': {'f150': [699, 763], 'f90': [667, 731]},
            '668': {'f150': [700, 764], 'f90': [668, 732]},
            '669': {'f150': [701, 765], 'f90': [669, 733]},
            '670': {'f150': [702, 766], 'f90': [670, 734]},
            '671': {'f150': [703, 767], 'f90': [671, 735]},
            '68': {'f150': [100, 164], 'f90': [68, 132]},
            '69': {'f150': [165, 229], 'f90': [69, 133]},
            '7': {'f150': [39, 103], 'f90': [7, 966]},
            '70': {'f150': [166, 230], 'f90': [70, 134]},
            '704': {'f150': [864, 928], 'f90': [704, 768]},
            '705': {'f150': [865, 929], 'f90': [705, 769]},
            '706': {'f150': [866, 930], 'f90': [706, 770]},
            '708': {'f150': [740, 804], 'f90': [708, 772]},
            '709': {'f150': [805, 869], 'f90': [709, 773]},
            '71': {'f150': [167, 231], 'f90': [71, 135]},
            '710': {'f150': [806, 870], 'f90': [710, 774]},
            '712': {'f150': [744, 808], 'f90': [712, 776]},
            '713': {'f150': [809, 873], 'f90': [713, 777]},
            '714': {'f150': [810, 874], 'f90': [714, 778]},
            '716': {'f150': [876, 940], 'f90': [716, 780]},
            '717': {'f150': [877, 941], 'f90': [717, 781]},
            '718': {'f150': [878, 942], 'f90': [718, 782]},
            '72': {'f150': [104, 168], 'f90': [72, 136]},
            '720': {'f150': [880, 944], 'f90': [720, 784]},
            '721': {'f150': [881, 945], 'f90': [721, 785]},
            '722': {'f150': [882, 946], 'f90': [722, 786]},
            '724': {'f150': [756, 820], 'f90': [724, 788]},
            '725': {'f150': [821, 885], 'f90': [725, 789]},
            '726': {'f150': [822, 886], 'f90': [726, 790]},
            '73': {'f150': [169, 233], 'f90': [73, 137]},
            '74': {'f150': [170, 234], 'f90': [74, 138]},
            '75': {'f150': [171, 235], 'f90': [75, 139]},
            '76': {'f150': [236, 300], 'f90': [76, 140]},
            '77': {'f150': [237, 301], 'f90': [77, 141]},
            '771': {'f150': [867, 931], 'f90': [771, 835]},
            '775': {'f150': [807, 871], 'f90': [775, 839]},
            '779': {'f150': [811, 875], 'f90': [779, 843]},
            '78': {'f150': [238, 302], 'f90': [78, 142]},
            '783': {'f150': [879, 943], 'f90': [783, 847]},
            '787': {'f150': [883, 947], 'f90': [787, 851]},
            '791': {'f150': [823, 887], 'f90': [791, 855]},
            '792': {'f150': [824, 888], 'f90': [792, 856]},
            '793': {'f150': [825, 889], 'f90': [793, 857]},
            '794': {'f150': [826, 890], 'f90': [794, 858]},
            '795': {'f150': [827, 891], 'f90': [795, 859]},
            '796': {'f150': [828, 892], 'f90': [796, 860]},
            '797': {'f150': [829, 893], 'f90': [797, 861]},
            '798': {'f150': [830, 894], 'f90': [798, 862]},
            '799': {'f150': [831, 895], 'f90': [799, 863]},
            '80': {'f150': [240, 304], 'f90': [80, 144]},
            '81': {'f150': [241, 305], 'f90': [81, 145]},
            '82': {'f150': [242, 306], 'f90': [82, 146]},
            '836': {'f150': [868, 932], 'f90': [836, 900]},
            '837': {'f150': [933, 997], 'f90': [837, 901]},
            '838': {'f150': [934, 998], 'f90': [838, 902]},
            '84': {'f150': [116, 180], 'f90': [84, 148]},
            '840': {'f150': [872, 936], 'f90': [840, 904]},
            '841': {'f150': [937, 1001], 'f90': [841, 905]},
            '842': {'f150': [938, 1002], 'f90': [842, 906]},
            '85': {'f150': [181, 245], 'f90': [85, 149]},
            '852': {'f150': [884, 948], 'f90': [852, 916]},
            '853': {'f150': [949, 1013], 'f90': [853, 917]},
            '854': {'f150': [950, 1014], 'f90': [854, 918]},
            '86': {'f150': [182, 246], 'f90': [86, 150]},
            '87': {'f150': [183, 247], 'f90': [87, 151]},
            '9': {'f150': [41, 105], 'f90': [9, 968]},
            '903': {'f150': [935, 999], 'f90': [903, 967]},
            '907': {'f150': [939, 1003], 'f90': [907, 971]},
            '919': {'f150': [951, 1015], 'f90': [919, 983]},
            '920': {'f150': [952, 1016], 'f90': [920, 984]},
            '921': {'f150': [953, 1017], 'f90': [921, 985]},
            '922': {'f150': [954, 1018], 'f90': [922, 986]},
            '923': {'f150': [955, 1019], 'f90': [923, 987]},
            '924': {'f150': [956, 1020], 'f90': [924, 988]},
            '925': {'f150': [957, 1021], 'f90': [925, 989]},
            '926': {'f150': [958, 1022], 'f90': [926, 990]},
            '927': {'f150': [959, 1023], 'f90': [927, 991]}
        }
        self.getAdjacentDetectors = self.adjacentDetectorGenerator()
        self.mask = mask

    def adjacentDetectorGenerator(self):
        """
        Generate a get_adjacent_pixels function
        Return a function to get adjacent detectors

        return: [int] function(int det)
        """
        detector_dir = self._array_info
        self._array_data = pd.read_csv(detector_dir, delim_whitespace=True, header=None)
        self._array_data.columns=['det_uid','row','col','freq','pol_family','array_x','array_y']
        # Get data from file
        ar = self._array_data[['array_x','array_y']].as_matrix()
        self._ar = ar

        # Find the adjacent detectors
        adj_dets = [None] * len(self._array_data) # Generate an empty list to store adjacent detector lists

        for i in range(len(self._array_data)):
            dis = np.dot((ar - ar[i,:])**2,[[1],[1]])
            _mask = ((dis < 0.6) & (dis > 0)).T & ((ar[:,0]!=0) | (ar[:,1]!=0))
            mask = _mask.flatten()
            indexes = np.where(mask == True)
            adj_dets[i]= list(list(indexes)[0]) # Normalize the np array output to list
        # Generate a function to access the data to make sure above procedures run once only
        def getAdjacentDetectors(detector):
            return adj_dets[detector]

        return getAdjacentDetectors

    def getPixels(self, mask=None):
        return [int(key) for key in self._pixel_dict]

    def getF90(self, pixel):
        if self.mask is not None:
            return [det for det in self._pixel_dict[str(pixel)]['f90'] if self.mask[det]==1]
        else:
            return self._pixel_dict[str(pixel)]['f90']
    
    def getF150(self, pixel):
        if self.mask is not None:
            return [det for det in self._pixel_dict[str(pixel)]['f150'] if self.mask[det]==1]
        else:
            return self._pixel_dict[str(pixel)]['f150'] 
    
    def getAdjacentPixels(self, pixel):
        all_adj_det = self.getAdjacentDetectors(pixel)
        return [int(det) for det in all_adj_det if str(det) in self._pixel_dict]
    
    def getPixelsWithinRadius(self, pixel, radius):
        ar = self._ar
        dist = np.sqrt(np.sum((ar - ar[pixel,:])**2, axis=1))
        return [det for det in np.arange(1055)[dist<radius] if str(det) in self._pixel_dict]
        
    def plot(self, pixels=None):
        plt.plot(self._array_data['array_x'], self._array_data['array_y'],'r.')
        if pixels:
            plt.plot(self._array_data['array_x'][pixels], self._array_data['array_y'][pixels],'b.')

    def getXY(self, pixel):
        return [self._array_data['array_x'][pixel], self._array_data['array_y'][pixel]]

    def getX(self, pixel):
        return self._array_data['array_x'][pixel]

    def getY(self, pixel):
        return self._array_data['array_y'][pixel]