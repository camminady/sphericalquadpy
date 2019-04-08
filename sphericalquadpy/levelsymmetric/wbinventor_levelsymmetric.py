# https://raw.githubusercontent.com/wbinventor/22.211-SN/master/quadrature.py
import numpy
from math import pi, sqrt


class LevelSymmetricQuadrature:
    """A level-symmetric quadrature set

    A class to generate level-symmetric quadrature sets for discrete 
    ordinates-based deterministic neutron transport. 

    This is adapted from Jeremy Roberts' implementation for the deterministic 
    neutron transport code suite, libdetran:

    https://github.com/robertsj/libdetran
    """

    def __init__(self):

        # Create a dictionary of values used to generate mu, eta, xi and
        # the corresponding weights for a level-symmetric quadrature.
        self.att = {}
        self.wtt = {}
        self.wtt_loc = {}

        # LQn S-2 Quadrature Set
        self.att[2] = numpy.array([0.577350269189625764509149])
        self.wtt[2] = numpy.array([1.000000000000000000000000])
        self.wtt_loc[2] = [0]

        # LQn S-4 Quadrature Set
        self.att[4] = numpy.array(
            [0.350021174581540677777041, 0.868890300722201205229788]
        )
        self.wtt[4] = numpy.array([0.333333333333333333333333])
        self.wtt_loc[4] = numpy.array([0, 0, 0])

        # LQn S-6 Quadrature Set
        self.att[6] = numpy.array(
            [
                0.266635401516704720331535,
                0.681507726536546927403750,
                0.926180935517489107558380,
            ]
        )
        self.wtt[6] = numpy.array(
            [0.176126130863383433783565, 0.157207202469949899549768]
        )
        self.wtt_loc[6] = numpy.array([0, 1, 0, 1, 1, 0])

        # LQn S-8 Quadrature Set
        self.att[8] = numpy.array(
            [
                0.218217890235992381266097,
                0.577350269189625764509149,
                0.786795792469443145800830,
                0.951189731211341853132399,
            ]
        )
        self.wtt[8] = numpy.array(
            [
                0.120987654320987654320988,
                0.0907407407407407407407407,
                0.0925925925925925925925926,
            ]
        )
        self.wtt_loc[8] = numpy.array([0, 1, 1, 0, 1, 2, 1, 1, 1, 0])

        # LQn S-10 Quadrature Set
        self.att[10] = numpy.array(
            [
                0.189321326478010476671494,
                0.508881755582618974382711,
                0.694318887594384317279217,
                0.839759962236684758403029,
                0.963490981110468484701598,
            ]
        )
        self.wtt[10] = numpy.array(
            [
                0.0893031479843567214704325,
                0.0725291517123655242296233,
                0.0450437674364086390490892,
                0.0539281144878369243545650,
            ]
        )
        self.wtt_loc[10] = numpy.array([0, 1, 2, 1, 0, 1, 3, 3, 1, 2, 3, 2, 1, 1, 0])

        # LQn S-12 Quadrature Set
        self.att[12] = numpy.array(
            [
                0.167212652822713264084504,
                0.459547634642594690016761,
                0.628019096642130901034766,
                0.760021014833664062877138,
                0.872270543025721502340662,
                0.971637719251358378302376,
            ]
        )
        self.wtt[12] = numpy.array(
            [
                0.0707625899700910439766549,
                0.0558811015648888075828962,
                0.0373376737588285824652402,
                0.0502819010600571181385765,
                0.0258512916557503911218290,
            ]
        )
        self.wtt_loc[12] = numpy.array(
            [0, 1, 2, 2, 1, 0, 1, 3, 4, 3, 1, 2, 4, 4, 2, 2, 3, 2, 1, 1, 0]
        )

        # LQn S-14 Quadrature Set
        self.att[14] = numpy.array(
            [
                0.151985861461031912404799,
                0.422156982304796966896263,
                0.577350269189625764509149,
                0.698892086775901338963210,
                0.802226255231412057244328,
                0.893691098874356784901111,
                0.976627152925770351762946,
            ]
        )
        self.wtt[14] = numpy.array(
            [
                0.0579970408969969964063611,
                0.0489007976368104874582568,
                0.0227935342411872473257345,
                0.0394132005950078294492985,
                0.0380990861440121712365891,
                0.0258394076418900119611012,
                0.00826957997262252825269908,
            ]
        )
        self.wtt_loc[14] = numpy.array(
            [
                0,
                1,
                2,
                3,
                2,
                1,
                0,
                1,
                4,
                5,
                5,
                4,
                1,
                2,
                5,
                6,
                5,
                2,
                3,
                5,
                5,
                3,
                2,
                4,
                2,
                1,
                1,
                0,
            ]
        )

        # LQn S-16 Quadrature Set
        self.att[16] = numpy.array(
            [
                0.138956875067780344591732,
                0.392289261444811712294197,
                0.537096561300879079878296,
                0.650426450628771770509703,
                0.746750573614681064580018,
                0.831996556910044145168291,
                0.909285500943725291652116,
                0.980500879011739882135849,
            ]
        )
        self.wtt[16] = numpy.array(
            [
                0.0489872391580385335008367,
                0.0413295978698440232405505,
                0.0203032007393652080748070,
                0.0265500757813498446015484,
                0.0379074407956004002099321,
                0.0135295047786756344371600,
                0.0326369372026850701318409,
                0.0103769578385399087825920,
            ]
        )
        self.wtt_loc[16] = numpy.array(
            [
                0,
                1,
                2,
                3,
                3,
                2,
                1,
                0,
                1,
                4,
                5,
                6,
                5,
                4,
                1,
                2,
                5,
                7,
                7,
                5,
                2,
                3,
                6,
                7,
                6,
                3,
                3,
                5,
                5,
                3,
                2,
                4,
                2,
                1,
                1,
                0,
            ]
        )

        # LQn S-18 Quadrature Set
        self.att[18] = numpy.array(
            [
                0.129344504545924818514086,
                0.368043816053393605686086,
                0.504165151725164054411848,
                0.610662549934881101060239,
                0.701166884252161909657019,
                0.781256199495913171286914,
                0.853866206691488372341858,
                0.920768021061018932899055,
                0.983127661236087115272518,
            ]
        )
        self.wtt[18] = numpy.array(
            [
                0.0422646448843821748535825,
                0.0376127473827281471532380,
                0.0122691351637405931037187,
                0.0324188352558815048715646,
                0.00664438614619073823264082,
                0.0312093838436551370068864,
                0.0160127252691940275641645,
                0.0200484595308572875885066,
                0.000111409402059638628382279,
                0.0163797038522425240494567,
            ]
        )
        self.wtt_loc[18] = numpy.array(
            [
                0,
                1,
                2,
                3,
                4,
                3,
                2,
                1,
                0,
                1,
                5,
                6,
                7,
                7,
                6,
                5,
                1,
                2,
                6,
                8,
                9,
                8,
                6,
                2,
                3,
                7,
                9,
                9,
                7,
                3,
                4,
                7,
                8,
                7,
                4,
                3,
                6,
                6,
                3,
                2,
                5,
                2,
                1,
                1,
                0,
            ]
        )

        # LQn S-20 Quadrature Set
        self.att[20] = numpy.array(
            [
                0.120603343036693597409418,
                0.347574292315847257336779,
                0.476519266143665680817278,
                0.577350269189625764509149,
                0.663020403653288019308783,
                0.738822561910371432904974,
                0.807540401661143067193530,
                0.870852583760463975580977,
                0.929863938955324566667817,
                0.985347485558646574628509,
            ]
        )
        self.wtt[20] = numpy.array(
            [
                0.0370210490604481342320295,
                0.0332842165376314841003910,
                0.0111738965965092519614021,
                0.0245177476959359285418987,
                0.0135924329650041789567081,
                0.0318029065936585971501960,
                0.00685492401402507781062634,
                0.0308105481755299327227893,
                -0.000139484716502602877593527,
                0.00544675187330776223879437,
                0.00474564692642379971238396,
                0.0277298541009064049325246,
            ]
        )
        self.wtt_loc[20] = numpy.array(
            [
                0,
                1,
                2,
                3,
                4,
                4,
                3,
                2,
                1,
                0,
                1,
                5,
                6,
                7,
                8,
                7,
                6,
                5,
                1,
                2,
                6,
                9,
                10,
                10,
                9,
                6,
                2,
                3,
                7,
                10,
                11,
                10,
                7,
                3,
                4,
                8,
                10,
                10,
                8,
                4,
                4,
                7,
                9,
                7,
                4,
                3,
                6,
                6,
                3,
                2,
                5,
                2,
                1,
                1,
                0,
            ]
        )

        # LQn S-22 Quadrature Set
        self.att[22] = numpy.array(
            [
                0.113888641383070838173488,
                0.330271760593086736334651,
                0.452977095507524183904005,
                0.548905330875560154226714,
                0.630401360620980621392149,
                0.702506006153654989703184,
                0.767869456282208576047898,
                0.828089557415325768804621,
                0.884217805921983001958912,
                0.936989829997455780115072,
                0.986944149751056870330152,
            ]
        )
        self.wtt[22] = numpy.array(
            [
                0.0329277718552552308051381,
                0.0309569328165031538543025,
                0.00577105953220643022391829,
                0.0316834548379952775919418,
                -0.00669350304140992494103696,
                0.0368381622687682466526634,
                0.0273139698006629537455404,
                0.0100962716435030437817055,
                0.0195181067555849392224199,
                0.0117224275470949786864925,
                -0.00442773155233893239996431,
                0.0156214785078803432781324,
                -0.0101774221315738297143270,
                0.0135061258938431808485310,
            ]
        )
        self.wtt_loc[22] = numpy.array(
            [
                0,
                1,
                2,
                3,
                4,
                5,
                4,
                3,
                2,
                1,
                0,
                1,
                6,
                7,
                8,
                9,
                9,
                8,
                7,
                6,
                1,
                2,
                7,
                10,
                11,
                12,
                11,
                10,
                7,
                2,
                3,
                8,
                11,
                13,
                13,
                11,
                8,
                3,
                4,
                9,
                12,
                13,
                12,
                9,
                4,
                5,
                9,
                11,
                11,
                9,
                5,
                4,
                8,
                10,
                8,
                4,
                3,
                7,
                7,
                3,
                2,
                6,
                2,
                1,
                1,
                0,
            ]
        )

        # LQn S-24 Quadrature Set
        self.att[24] = numpy.array(
            [
                0.107544208775147285552086,
                0.315151630853896874875332,
                0.432522073446742487657060,
                0.524242441631224399254880,
                0.602150256328323868809286,
                0.671073561381361944701265,
                0.733549261041044861004094,
                0.791106384731321324814121,
                0.844750913317919895113069,
                0.895186516397704814461305,
                0.942928254285052510917188,
                0.988366574868785749937406,
            ]
        )
        self.wtt[24] = numpy.array(
            [
                0.0295284942030736546025272,
                0.0281530651743695026834932,
                0.00519730128072174996473824,
                0.0259897467786242920448933,
                0.00146378160153344429844948,
                0.0166609651269037212368055,
                0.0281343344093849194875108,
                0.00214364311909247909952968,
                0.0331943417648083019611294,
                -0.0142483904822400753741381,
                0.0416812529998231580614934,
                0.00323522898964475022578598,
                0.000813552611571786631179287,
                0.00228403610697848813660369,
                0.0338971925236628645848112,
                -0.00644725595698339499416262,
            ]
        )
        self.wtt_loc[24] = numpy.array(
            [
                0,
                1,
                2,
                3,
                4,
                5,
                5,
                4,
                3,
                2,
                1,
                0,
                1,
                6,
                7,
                8,
                9,
                10,
                9,
                8,
                7,
                6,
                1,
                2,
                7,
                11,
                12,
                13,
                13,
                12,
                11,
                7,
                2,
                3,
                8,
                12,
                14,
                15,
                14,
                12,
                8,
                3,
                4,
                9,
                13,
                15,
                15,
                13,
                9,
                4,
                5,
                10,
                13,
                14,
                13,
                10,
                5,
                5,
                9,
                12,
                12,
                9,
                5,
                4,
                8,
                11,
                8,
                4,
                3,
                7,
                7,
                3,
                2,
                6,
                2,
                1,
                1,
                0,
            ]
        )

    def getQuadratureSet(self, order=4):

        # Initialize a dictionary to contain all of the information for
        # a level-symmetric quadrature of some order (2-24)
        quad = {}
        quad["order"] = int(order)
        quad["num polar"] = int(order / 2)
        quad["num angles"] = int(
            2 * quad["num polar"] * (2 * quad["num polar"] + 2) / 8 * 4
        )
        quad["num angles per octant"] = int(quad["num angles"] / 4)

        print
        "Generating level-symmetric quadrature with %d angles" % (quad["num angles"])

        quad["mu"] = numpy.zeros(quad["num angles per octant"])
        quad["eta"] = numpy.zeros(quad["num angles per octant"])
        quad["xi"] = numpy.zeros(quad["num angles per octant"])
        quad["weight"] = numpy.zeros(quad["num angles per octant"])

        # Loop over all angles in an octant
        m = 0
        for i in range(int(order / 2)):
            for j in range(int(order / 2) - i):
                quad["mu"][m] = self.att[order][i]
                quad["eta"][m] = self.att[order][j]
                quad["xi"][m] = sqrt(1.0 - quad["mu"][m] ** 2 - quad["eta"][m] ** 2)
                quad["weight"][m] = self.wtt[order][self.wtt_loc[order][m]] * pi
                m += 1

        return quad

    # get quadrature for all 8 octants
    def getQuadratureSetAll8octants(self, quadrature1octant):
        n = len(quadrature1octant["mu"])
        xyz = numpy.zeros((8 * n, 3))
        w = numpy.zeros(8 * n)

        x = quadrature1octant["mu"]
        y = quadrature1octant["eta"]
        z = quadrature1octant["xi"]

        xyz[(0 * n) : (1 * n), 0] = x
        xyz[(0 * n) : (1 * n), 1] = y
        xyz[(0 * n) : (1 * n), 2] = z

        xyz[(1 * n) : (2 * n), 0] = -x
        xyz[(1 * n) : (2 * n), 1] = y
        xyz[(1 * n) : (2 * n), 2] = z

        xyz[(2 * n) : (3 * n), 1] = -y
        xyz[(2 * n) : (3 * n), 0] = x
        xyz[(2 * n) : (3 * n), 2] = z

        xyz[(3 * n) : (4 * n), 0] = -x
        xyz[(3 * n) : (4 * n), 1] = -y
        xyz[(3 * n) : (4 * n), 2] = z

        xyz[(4 * n) : (5 * n), 0] = x
        xyz[(4 * n) : (5 * n), 1] = y
        xyz[(4 * n) : (5 * n), 2] = -z

        xyz[(5 * n) : (6 * n), 0] = -x
        xyz[(5 * n) : (6 * n), 1] = y
        xyz[(5 * n) : (6 * n), 2] = -z

        xyz[(6 * n) : (7 * n), 1] = -y
        xyz[(6 * n) : (7 * n), 0] = x
        xyz[(6 * n) : (7 * n), 2] = -z

        xyz[(7 * n) : (8 * n), 0] = -x
        xyz[(7 * n) : (8 * n), 1] = -y
        xyz[(7 * n) : (8 * n), 2] = -z

        w = numpy.repeat(quadrature1octant["weight"], 8)
        return xyz, w
