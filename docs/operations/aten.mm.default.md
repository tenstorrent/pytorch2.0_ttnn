### aten.mm.default
|     | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|----:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1024]> mat2 = ?     | Done     | Done       | 0.999966603114867  | 0      |
|   1 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1280]> mat2 = ?     | Done     | Done       | 0.9999661547582631 | 0      |
|   2 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1536]> mat2 = ?     | Done     | Done       | 0.9999710077495829 | 0      |
|   3 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 2048]> mat2 = ?     | Done     | Done       | 0.9999665703423878 | 0      |
|   4 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 512]> mat2 = ?      | Done     | Done       | 0.9998724278248905 | 0      |
|   5 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 768]> mat2 = ?      | Done     | Done       | 0.9999640547884255 | 0      |
|   6 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?     | Unknown  | Done       | 0.9999660839405496 | 0      |
|   7 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?     | Unknown  | Done       | 0.999965223554218  | 0      |
|   8 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 32128]> mat2 = ?    | Unknown  | Done       | 0.9998404700092384 | 0      |
|   9 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?     | Unknown  | Done       | 0.9999646253250931 | 0      |
|  10 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?      | Unknown  | Done       | 0.9998651192247636 | 0      |
|  11 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 128]> mat2 = ?          | Done     | Done       | 0.9999938445281409 | 0      |
|  12 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 64]> mat2 = ?         | Done     | Done       | 0.9999595674542378 | 0      |
|  13 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 784]> mat2 = ?        | Done     | Done       | 0.9999781380443863 | 0      |
|  14 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 9216]> mat2 = ?       | Done     | Done       | 0.9999821366761551 | 0      |
|  15 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 3]> mat2 = ?            | Done     | Done       | 1.0                | 0      |
|  16 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 64]> mat2 = ?           | Done     | Done       | 0.9999940334803832 | 0      |
|  17 | Tensor<[1, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?      | Unknown  | Done       | 0.99962477723247   | 0      |
|  18 | Tensor<[1, 21843]> self = ?,<br>Tensor<[21843, 768]> mat2 = ?    | Done     | Done       | 0.9882038186019169 | 0      |
|  19 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?            | Unknown  | Done       | 0.9999946420186739 | 0      |
|  20 | Tensor<[1, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?      | Unknown  | Done       | 0.9999478361324728 | 0      |
|  21 | Tensor<[1, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?        | Unknown  | Unknown    | N/A                | N/A    |
|  22 | Tensor<[1, 3]> self = ?,<br>Tensor<[3, 12]> mat2 = ?             | Done     | Done       | 0.9999967231912887 | 0      |
|  23 | Tensor<[1, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?     | Unknown  | Done       | 0.9999314071505113 | 0      |
|  24 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?       | Unknown  | Done       | 0.9999684936776113 | 0      |
|  25 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?       | Unknown  | Done       | 0.9999714792018362 | 0      |
|  26 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?      | Unknown  | Done       | 0.9999298193242496 | 0      |
|  27 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?        | Unknown  | Unknown    | N/A                | N/A    |
|  28 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?      | Unknown  | Done       | 0.9999295328284411 | 0      |
|  29 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?        | Unknown  | Done       | 0.9999175690689696 | 0      |
|  30 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?        | Unknown  | Done       | 0.9999709259385708 | 0      |
|  31 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 128]> mat2 = ?          | Done     | Done       | 0.9999906959227935 | 0      |
|  32 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 12]> mat2 = ?           | Done     | Done       | 0.9999927745323448 | 0      |
|  33 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?       | Unknown  | Done       | 0.9999696964971563 | 0      |
|  34 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 32128]> mat2 = ?      | Unknown  | Done       | 0.9998867545201684 | 0      |
|  35 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?      | Unknown  | Done       | 0.999888556093457  | 0      |
|  36 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?        | Done     | Done       | 0.9998883760594304 | 0      |
|  37 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?      | Unknown  | Done       | 0.999886393408029  | 0      |
|  38 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?        | Unknown  | Done       | 0.999967931949236  | 0      |
|  39 | Tensor<[1, 784]> self = ?,<br>Tensor<[784, 128]> mat2 = ?        | Done     | Done       | 0.9998912486958579 | 0      |
|  40 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?    | Unknown  | Done       | 0.9999660744874969 | 0      |
|  41 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?    | Unknown  | Done       | 0.9999651738059586 | 0      |
|  42 | Tensor<[10, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?           | Done     | Done       | 0.9999966149295578 | 0      |
|  43 | Tensor<[10, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?     | Unknown  | Done       | 0.999596183555748  | 0      |
|  44 | Tensor<[10, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Unknown  | Done       | 0.9999448057892468 | 0      |
|  45 | Tensor<[10, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?    | Unknown  | Done       | 0.9999332956038989 | 0      |
|  46 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?      | Unknown  | Done       | 0.9999715432465851 | 0      |
|  47 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?       | Unknown  | Done       | 0.9999337049541837 | 0      |
|  48 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?      | Unknown  | Done       | 0.9999686365280023 | 0      |
|  49 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.9999694238400789 | 0      |
|  50 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1024]> mat2 = ?        | Done     | Done       | 0.9999959836870003 | 0      |
|  51 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1280]> mat2 = ?        | Done     | Done       | 0.9999958066004618 | 0      |
|  52 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1536]> mat2 = ?        | Done     | Done       | 0.9999958276836025 | 0      |
|  53 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 2048]> mat2 = ?        | Done     | Done       | 0.9999960736892088 | 0      |
|  54 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?         | Done     | Done       | 0.999995987154305  | 0      |
|  55 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?         | Done     | Done       | 0.9999960483797995 | 0      |
|  56 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?     | Done     | Done       | 0.9999768813864206 | 0      |
|  57 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ?     | Done     | Done       | 0.999976863254509  | 0      |
|  58 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 640]> mat2 = ?     | Done     | Done       | 0.9999768570105544 | 0      |
|  59 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?    | Done     | Done       | 0.9999707451627015 | 0      |
|  60 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 4096]> mat2 = ?    | Done     | Done       | 0.9999706730616456 | 0      |
|  61 | Tensor<[1024, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Done     | Done       | 0.9999756109428068 | 0      |
|  62 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?     | Done     | Done       | 0.9999731159721988 | 0      |
|  63 | Tensor<[1024, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?     | Done     | Done       | 0.9999715399436719 | 0      |
|  64 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 160]> mat2 = ?     | Done     | Done       | 0.9999696231045203 | 0      |
|  65 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 3]> mat2 = ?             | Done     | Done       | 0.999999655083991  | 0      |
|  66 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?            | Done     | Done       | 0.9999958346222593 | 0      |
|  67 | Tensor<[128, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?   | Done     | Done       | 0.9919030504035383 | 0      |
|  68 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?           | Done     | Done       | 0.9999957939291172 | 0      |
|  69 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 784]> mat2 = ?          | Done     | Done       | 0.9999962785998122 | 0      |
|  70 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 9216]> mat2 = ?         | Done     | Done       | 0.9999957434553594 | 0      |
|  71 | Tensor<[14, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?     | Unknown  | Done       | 0.9996188175069639 | 0      |
|  72 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?      | Unknown  | Done       | 0.999971118314418  | 0      |
|  73 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?       | Unknown  | Done       | 0.9999321343915788 | 0      |
|  74 | Tensor<[15, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  75 | Tensor<[15, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?       | Unknown  | Done       | 0.9999474034946255 | 0      |
|  76 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?      | Unknown  | Done       | 0.999971000104728  | 0      |
|  77 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?       | Unknown  | Done       | 0.9999294599244183 | 0      |
|  78 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  | Done       | 0.9999634118380057 | 0      |
|  79 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?    | Done     | Done       | 0.9998362201031278 | 0      |
|  80 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 640]> mat2 = ?    | Done     | Done       | 0.9999654166776603 | 0      |
|  81 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?     | Done     | Done       | 0.9999751776917996 | 0      |
|  82 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 160]> mat2 = ?      | Done     | Done       | 0.9999650635562789 | 0      |
|  83 | Tensor<[16384, 128]> self = ?,<br>Tensor<[128, 32]> mat2 = ?     | Done     | Done       | 0.9999807532072336 | 0      |
|  84 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 128]> mat2 = ?      | Done     | Done       | 0.9999911973671527 | 0      |
|  85 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?      | Done     | Done       | 0.999991214644356  | 0      |
|  86 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     | Done       | 0.9999911334188814 | 0      |
|  87 | Tensor<[19, 1024]> self = ?,<br>Tensor<[1024, 256008]> mat2 = ?  | Done     | Done       | 0.9998388733023666 | 0      |
|  88 | Tensor<[196, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?    | Done     | Done       | 0.9998383245498451 | 0      |
|  89 | Tensor<[196, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     | Done       | 0.9999438917930004 | 0      |
|  90 | Tensor<[196, 384]> self = ?,<br>Tensor<[384, 768]> mat2 = ?      | Done     | Done       | 0.9999728196397403 | 0      |
|  91 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     | Done       | 0.9999682016300823 | 0      |
|  92 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?      | Done     | Done       | 0.9998870362585428 | 0      |
|  93 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Done     | Done       | 0.999965770427472  | 0      |
|  94 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Done     | Done       | 0.9999655925941392 | 0      |
|  95 | Tensor<[197, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     | Done       | 0.9999442219647527 | 0      |
|  96 | Tensor<[197, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Done     | Done       | 0.9999343365565796 | 0      |
|  97 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     | Done       | 0.9999683710019515 | 0      |
|  98 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Done     | Done       | 0.9999685701339095 | 0      |
|  99 | Tensor<[2, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?            | Unknown  | Done       | 0.9999961328326341 | 0      |
| 100 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?          | Done     | Done       | 1.0                | 0      |
| 101 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?        | Done     | Done       | 0.999919021865926  | 0      |
| 102 | Tensor<[2048, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?       | Unknown  | Done       | 0.9999943608125529 | 0      |
| 103 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ?     | Done     | Done       | 0.999968324277907  | 0      |
| 104 | Tensor<[21843, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?        | Done     | Done       | 0.9999957767997688 | 0      |
| 105 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?       | Done     | Done       | 0.9999249075071667 | 0      |
| 106 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 16]> mat2 = ?       | Done     | Done       | 0.9999305196592176 | 0      |
| 107 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?       | Done     | Done       | 0.9999310779736179 | 0      |
| 108 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 32]> mat2 = ?       | Done     | Done       | 0.9999261196045078 | 0      |
| 109 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?        | Done     | Done       | 0.9999220094016643 | 0      |
| 110 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?        | Done     | Done       | 0.9999330816263738 | 0      |
| 111 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?        | Done     | Done       | 0.9999305909794697 | 0      |
| 112 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 8]> mat2 = ?        | Done     | Done       | 0.9999272930433901 | 0      |
| 113 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?    | Done     | Done       | 0.9998396595176612 | 0      |
| 114 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 256]> mat2 = ?    | Done     | Done       | 0.9998385169350426 | 0      |
| 115 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?    | Done     | Done       | 0.9998398678051998 | 0      |
| 116 | Tensor<[256, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?      | Done     | Done       | 0.9999766491200197 | 0      |
| 117 | Tensor<[256, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?   | Done     | Done       | 0.9921462940206537 | 0      |
| 118 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?     | Done     | Done       | 0.9999753785398136 | 0      |
| 119 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?      | Done     | Done       | 0.9999649295236418 | 0      |
| 120 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 512]> mat2 = ?      | Done     | Done       | 0.9999652749412271 | 0      |
| 121 | Tensor<[256, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?         | Done     | Done       | 0.9999912494671579 | 0      |
| 122 | Tensor<[256, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?     | Done     | Done       | 0.9990010642337545 | 0      |
| 123 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?      | Done     | Done       | 0.9999282991400338 | 0      |
| 124 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?      | Done     | Done       | 0.9999713956397661 | 0      |
| 125 | Tensor<[256, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?         | Done     | Done       | 0.9999878386325871 | 0      |
| 126 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?      | Done     | Done       | 0.9998860612929579 | 0      |
| 127 | Tensor<[3, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?             | Done     | Done       | 0.9999962735241897 | 0      |
| 128 | Tensor<[3072, 196]> self = ?,<br>Tensor<[196, 768]> mat2 = ?     | Done     | Done       | 0.9999708901505346 | 0      |
| 129 | Tensor<[3072, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?     | Done     | Done       | 0.9999706966753027 | 0      |
| 130 | Tensor<[3072, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?       | Unknown  | Done       | 0.9999859291835546 | 0      |
| 131 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ?  | Done     | Done       | 0.9997304195715929 | 0      |
| 132 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 128]> mat2 = ?   | Done     | Done       | 0.9922598475027838 | 0      |
| 133 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?    | Done     | Done       | 0.9921630187536548 | 0      |
| 134 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 16384]> mat2 = ?     | Done     | Done       | 0.9999651966513048 | 0      |
| 135 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 32]> mat2 = ?        | Done     | Done       | 0.9999652247128255 | 0      |
| 136 | Tensor<[384, 768]> self = ?,<br>Tensor<[768, 196]> mat2 = ?      | Done     | Done       | 0.9998860351110557 | 0      |
| 137 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?      | Unknown  | Done       | 0.9998871694013506 | 0      |
| 138 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?        | Unknown  | Done       | 0.9999684217795306 | 0      |
| 139 | Tensor<[4096, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?    | Done     | Done       | 0.9999706627319004 | 0      |
| 140 | Tensor<[4096, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?      | Done     | Done       | 0.999975347751539  | 0      |
| 141 | Tensor<[4096, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?     | Unknown  | Done       | 0.9999739659619848 | 0      |
| 142 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?       | Done     | Done       | 0.9999864261864694 | 0      |
| 143 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     | Done       | 0.9999864330844024 | 0      |
| 144 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?     | Unknown  | Done       | 0.9998864221668918 | 0      |
| 145 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.999968163395098  | 0      |
| 146 | Tensor<[49, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ?     | Done     | Done       | 0.9999610316175939 | 0      |
| 147 | Tensor<[49, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ?    | Done     | Done       | 0.9999553528271644 | 0      |
| 148 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?     | Unknown  | Done       | 0.9999673501859437 | 0      |
| 149 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?     | Unknown  | Done       | 0.9999656694398888 | 0      |
| 150 | Tensor<[50, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Unknown  | Done       | 0.9999438155694115 | 0      |
| 151 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?      | Unknown  | Done       | 0.9999684762903536 | 0      |
| 152 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.9999683396335357 | 0      |
| 153 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 2048]> mat2 = ?       | Unknown  | Done       | 0.9999943475901997 | 0      |
| 154 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?        | Unknown  | Done       | 0.9999943596868709 | 0      |
| 155 | Tensor<[512, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?          | Unknown  | Done       | 0.9999957628264668 | 0      |
| 156 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?      | Done     | Done       | 0.9999654911141963 | 0      |
| 157 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 768]> mat2 = ?      | Done     | Done       | 0.9999753509581015 | 0      |
| 158 | Tensor<[512, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?          | Unknown  | Done       | 0.9999952625983484 | 0      |
| 159 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?     | Unknown  | Done       | 0.9998375756053308 | 0      |
| 160 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?      | Unknown  | Done       | 0.9999714793235094 | 0      |
| 161 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?     | Unknown  | Done       | 0.9999290564745356 | 0      |
| 162 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ?     | Done     | Done       | 0.9999602260314291 | 0      |
| 163 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?           | Done     | Done       | 0.9999964133541253 | 0      |
| 164 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?            | Done     | Done       | 0.9999974620238082 | 0      |
| 165 | Tensor<[64, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ?    | Done     | Done       | 0.9999548381731093 | 0      |
| 166 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 4096]> mat2 = ?      | Done     | Done       | 0.9999751479100626 | 0      |
| 167 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?        | Done     | Done       | 0.9999653356702656 | 0      |
| 168 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 256]> mat2 = ?     | Done     | Done       | 0.9990236818570766 | 0      |
| 169 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?      | Done     | Done       | 0.9989971593968098 | 0      |
| 170 | Tensor<[640, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?    | Done     | Done       | 0.9999657224577685 | 0      |
| 171 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ?          | Done     | Done       | 0.9998244780431508 | 0      |
| 172 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 3072]> mat2 = ?     | Done     | Done       | 0.9999707747927625 | 0      |
| 173 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ?      | Done     | Done       | 0.9999708646826942 | 0      |
| 174 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 3072]> mat2 = ?     | Done     | Done       | 0.9999706975927035 | 0      |
| 175 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?      | Done     | Done       | 0.9999707947887286 | 0      |
| 176 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 3072]> mat2 = ?       | Unknown  | Done       | 0.9999860097929969 | 0      |
| 177 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?        | Unknown  | Done       | 0.9999859949709962 | 0      |
| 178 | Tensor<[784, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?          | Done     | Done       | 0.9999959124382359 | 0      |
| 179 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?      | Done     | Done       | 0.9999728750234647 | 0      |
| 180 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?      | Done     | Done       | 0.9999714582142675 | 0      |
| 181 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 1280]> mat2 = ?       | Unknown  | Done       | 0.9999681833273466 | 0      |
| 182 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 320]> mat2 = ?        | Unknown  | Done       | 0.9998860098279143 | 0      |
| 183 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 640]> mat2 = ?        | Unknown  | Done       | 0.9999694523112039 | 0      |
| 184 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?      | Done     | Done       | 0.9999753749389105 | 0      |
| 185 | Tensor<[s0*s1, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 186 | Tensor<[s0*s1, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 187 | Tensor<[s1*s2, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 188 | Tensor<[s1*s2, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 189 | Tensor<[s1*s2, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |

