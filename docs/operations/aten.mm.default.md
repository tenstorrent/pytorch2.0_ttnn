### aten.mm.default
|     | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|----:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1024]> mat2 = ?     | Done     | Done       | 0.9999700464415966 | 0      |
|   1 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1280]> mat2 = ?     | Done     | Done       | 0.9999678711623481 | 0      |
|   2 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1536]> mat2 = ?     | Done     | Done       | 0.9999684475538908 | 0      |
|   3 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 2048]> mat2 = ?     | Done     | Done       | 0.9999672391342413 | 0      |
|   4 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 512]> mat2 = ?      | Done     | Done       | 0.9998462102326802 | 0      |
|   5 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 768]> mat2 = ?      | Done     | Done       | 0.9999663154846355 | 0      |
|   6 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?     | Unknown  | Done       | 0.9999628368204216 | 0      |
|   7 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?     | Unknown  | Done       | 0.9999655288413121 | 0      |
|   8 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 32128]> mat2 = ?    | Unknown  | Done       | 0.9998430689023616 | 0      |
|   9 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?     | Unknown  | Done       | 0.9999657324735283 | 0      |
|  10 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?      | Unknown  | Done       | 0.9998483242135426 | 0      |
|  11 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 128]> mat2 = ?          | Done     | Done       | 0.9999951255174983 | 0      |
|  12 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 64]> mat2 = ?         | Done     | Done       | 0.9999775978516094 | 0      |
|  13 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 784]> mat2 = ?        | Done     | Done       | 0.999980849862121  | 0      |
|  14 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 9216]> mat2 = ?       | Done     | Done       | 0.9999798525976512 | 0      |
|  15 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 3]> mat2 = ?            | Done     | Done       | 0.9999997305280204 | 0      |
|  16 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 64]> mat2 = ?           | Done     | Done       | 0.9999921385120503 | 0      |
|  17 | Tensor<[1, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?      | Unknown  | Done       | 0.9996903205941744 | 0      |
|  18 | Tensor<[1, 21843]> self = ?,<br>Tensor<[21843, 768]> mat2 = ?    | None     | Fallback   | 1.0                | -1     |
|  19 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?            | Unknown  | Done       | 0.9999954448388011 | 0      |
|  20 | Tensor<[1, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?      | Unknown  | Done       | 0.9999495623374661 | 0      |
|  21 | Tensor<[1, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?        | Unknown  | Done       | 0.9999485304835309 | 0      |
|  22 | Tensor<[1, 3]> self = ?,<br>Tensor<[3, 12]> mat2 = ?             | Done     | Done       | 0.9999892103617755 | 0      |
|  23 | Tensor<[1, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?     | Unknown  | Done       | 0.999935947057528  | 0      |
|  24 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?       | Unknown  | Done       | 0.9999672974073585 | 0      |
|  25 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?       | Unknown  | Done       | 0.9999734173709773 | 0      |
|  26 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?      | Unknown  | Done       | 0.9999273344134187 | 0      |
|  27 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?        | Unknown  | Done       | 0.9999459168321853 | 0      |
|  28 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?      | Unknown  | Done       | 0.9999307410512481 | 0      |
|  29 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?        | Unknown  | Done       | 0.9999201781115572 | 0      |
|  30 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?        | Unknown  | Done       | 0.9999745677272879 | 0      |
|  31 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 128]> mat2 = ?          | Done     | Done       | 0.999986301498178  | 0      |
|  32 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 12]> mat2 = ?           | Done     | Done       | 0.9999919718458556 | 0      |
|  33 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?       | Unknown  | Done       | 0.9999694180583341 | 0      |
|  34 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 32128]> mat2 = ?      | Unknown  | Done       | 0.9998884173811585 | 0      |
|  35 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?      | Unknown  | Done       | 0.9998796003538354 | 0      |
|  36 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?        | Done     | Done       | 0.9998856768186984 | 0      |
|  37 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?      | Unknown  | Done       | 0.999887767056337  | 0      |
|  38 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?        | Unknown  | Done       | 0.999968002489629  | 0      |
|  39 | Tensor<[1, 784]> self = ?,<br>Tensor<[784, 128]> mat2 = ?        | Done     | Done       | 0.999854844554321  | 0      |
|  40 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?    | Unknown  | Done       | 0.9999650217648985 | 0      |
|  41 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?    | Unknown  | Done       | 0.9999651042999242 | 0      |
|  42 | Tensor<[10, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?           | Done     | Done       | 0.9999966390335048 | 0      |
|  43 | Tensor<[10, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?     | Unknown  | Done       | 0.9996122714383152 | 0      |
|  44 | Tensor<[10, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Unknown  | Done       | 0.9999435947699222 | 0      |
|  45 | Tensor<[10, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?    | Unknown  | Done       | 0.9999320731767305 | 0      |
|  46 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?      | Unknown  | Done       | 0.9999716440907215 | 0      |
|  47 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?       | Unknown  | Done       | 0.9999302367133108 | 0      |
|  48 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?      | Unknown  | Done       | 0.9999685093150535 | 0      |
|  49 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.9999675308955925 | 0      |
|  50 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1024]> mat2 = ?        | Done     | Done       | 0.9999961107203191 | 0      |
|  51 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1280]> mat2 = ?        | Done     | Done       | 0.9999959013155703 | 0      |
|  52 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1536]> mat2 = ?        | Done     | Done       | 0.9999959293434421 | 0      |
|  53 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 2048]> mat2 = ?        | Done     | Done       | 0.99999604938135   | 0      |
|  54 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?         | Done     | Done       | 0.9999958873636614 | 0      |
|  55 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?         | Done     | Done       | 0.9999958684646094 | 0      |
|  56 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?     | Done     | Done       | 0.9999770629221625 | 0      |
|  57 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ?     | Done     | Done       | 0.9999768628513848 | 0      |
|  58 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 640]> mat2 = ?     | Done     | Done       | 0.9999770741209211 | 0      |
|  59 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?    | Done     | Done       | 0.9999708449712039 | 0      |
|  60 | Tensor<[1024, 197]> self = ?,<br>Tensor<[197, 4096]> mat2 = ?    | Done     | Done       | 0.9999708039427609 | 0      |
|  61 | Tensor<[1024, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Done     | Done       | 0.9999755568019029 | 0      |
|  62 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?     | Done     | Done       | 0.9999729319326607 | 0      |
|  63 | Tensor<[1024, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?     | Done     | Done       | 0.9999713414431731 | 0      |
|  64 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 160]> mat2 = ?     | Done     | Done       | 0.9999697930184783 | 0      |
|  65 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 3]> mat2 = ?             | Done     | Done       | 0.9999963464228881 | 0      |
|  66 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?            | Done     | Done       | 0.9999956749708057 | 0      |
|  67 | Tensor<[128, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?   | Done     | Done       | 0.9921570712530501 | 0      |
|  68 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?           | Done     | Done       | 0.9999955679936674 | 0      |
|  69 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 784]> mat2 = ?          | Done     | Done       | 0.999996040864063  | 0      |
|  70 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 9216]> mat2 = ?         | Done     | Done       | 0.9999960806556069 | 0      |
|  71 | Tensor<[14, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?     | Unknown  | Done       | 0.9996076781476445 | 0      |
|  72 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?      | Unknown  | Done       | 0.9999704328587543 | 0      |
|  73 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?       | Unknown  | Done       | 0.9999318159042769 | 0      |
|  74 | Tensor<[15, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?     | Unknown  | Done       | 0.999835738613014  | 0      |
|  75 | Tensor<[15, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?       | Unknown  | Done       | 0.999948646711155  | 0      |
|  76 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?      | Unknown  | Done       | 0.999971228306865  | 0      |
|  77 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?       | Unknown  | Done       | 0.9999259347537044 | 0      |
|  78 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?     | Unknown  | Done       | 0.9999634061090665 | 0      |
|  79 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?    | Done     | Done       | 0.9998386396583862 | 0      |
|  80 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 640]> mat2 = ?    | Done     | Done       | 0.9999655205926631 | 0      |
|  81 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?     | Done     | Done       | 0.9999753069143589 | 0      |
|  82 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 160]> mat2 = ?      | Done     | Done       | 0.9999664236039882 | 0      |
|  83 | Tensor<[16384, 128]> self = ?,<br>Tensor<[128, 32]> mat2 = ?     | Done     | Done       | 0.9999809299652597 | 0      |
|  84 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 128]> mat2 = ?      | Done     | Done       | 0.9999911975182004 | 0      |
|  85 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?      | Done     | Done       | 0.9999912499479564 | 0      |
|  86 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?       | Done     | Done       | 0.9999912153314957 | 0      |
|  87 | Tensor<[19, 1024]> self = ?,<br>Tensor<[1024, 256008]> mat2 = ?  | Done     | Done       | 0.9998386757466566 | 0      |
|  88 | Tensor<[196, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?    | Done     | Done       | 0.9998404487361485 | 0      |
|  89 | Tensor<[196, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     | Done       | 0.9999448811369949 | 0      |
|  90 | Tensor<[196, 384]> self = ?,<br>Tensor<[384, 768]> mat2 = ?      | Done     | Done       | 0.99997312598488   | 0      |
|  91 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     | Done       | 0.9999683829163368 | 0      |
|  92 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?      | Done     | Done       | 0.9998871395531654 | 0      |
|  93 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Done     | Done       | 0.9999655036592018 | 0      |
|  94 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Done     | Done       | 0.9999656683675059 | 0      |
|  95 | Tensor<[197, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     | Done       | 0.9999446476386364 | 0      |
|  96 | Tensor<[197, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Done     | Done       | 0.9999336184546662 | 0      |
|  97 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     | Done       | 0.9999684160264077 | 0      |
|  98 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Done     | Done       | 0.999968393330127  | 0      |
|  99 | Tensor<[2, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?            | Unknown  | Done       | 0.9999954631690166 | 0      |
| 100 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?          | Done     | Done       | 1.0                | 0      |
| 101 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?        | Done     | Done       | 0.9999255820832933 | 0      |
| 102 | Tensor<[2048, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?       | Unknown  | Done       | 0.9999943691565366 | 0      |
| 103 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ?     | Done     | Done       | 0.9999683688483806 | 0      |
| 104 | Tensor<[21843, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?        | Done     | Done       | 0.9999960143968931 | 0      |
| 105 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?       | Done     | Done       | 0.9999312370097972 | 0      |
| 106 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 16]> mat2 = ?       | Done     | Done       | 0.9999286695313347 | 0      |
| 107 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?       | Done     | Done       | 0.9999316505128056 | 0      |
| 108 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 32]> mat2 = ?       | Done     | Done       | 0.9999304383614006 | 0      |
| 109 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?        | Done     | Done       | 0.999909646360548  | 0      |
| 110 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?        | Done     | Done       | 0.9999326947988443 | 0      |
| 111 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?        | Done     | Done       | 0.9999258593404746 | 0      |
| 112 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 8]> mat2 = ?        | Done     | Done       | 0.9999294755493665 | 0      |
| 113 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?    | Done     | Done       | 0.9998352711773296 | 0      |
| 114 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 256]> mat2 = ?    | Done     | Done       | 0.9998387667156543 | 0      |
| 115 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?    | Done     | Done       | 0.9998371862899272 | 0      |
| 116 | Tensor<[256, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?      | Done     | Done       | 0.9999769203810965 | 0      |
| 117 | Tensor<[256, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?   | Done     | Done       | 0.9920696419216948 | 0      |
| 118 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?     | Done     | Done       | 0.9999755973782486 | 0      |
| 119 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?      | Done     | Done       | 0.9999649495425592 | 0      |
| 120 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 512]> mat2 = ?      | Done     | Done       | 0.9999652917852907 | 0      |
| 121 | Tensor<[256, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?         | Done     | Done       | 0.9999912795147118 | 0      |
| 122 | Tensor<[256, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?     | Done     | Done       | 0.9990196848486109 | 0      |
| 123 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?      | Done     | Done       | 0.9999290629591271 | 0      |
| 124 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?      | Done     | Done       | 0.9999713976726785 | 0      |
| 125 | Tensor<[256, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?         | Done     | Done       | 0.999987831656986  | 0      |
| 126 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?      | Done     | Done       | 0.9998866428911919 | 0      |
| 127 | Tensor<[3, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?             | Done     | Done       | 0.9999923475119511 | 0      |
| 128 | Tensor<[3072, 196]> self = ?,<br>Tensor<[196, 768]> mat2 = ?     | Done     | Done       | 0.9999707825685432 | 0      |
| 129 | Tensor<[3072, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?     | Done     | Done       | 0.9999706500592627 | 0      |
| 130 | Tensor<[3072, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?       | Unknown  | Done       | 0.9999859298310236 | 0      |
| 131 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ?  | Done     | Done       | 0.9997303593567773 | 0      |
| 132 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 128]> mat2 = ?   | Done     | Done       | 0.9920582072144857 | 0      |
| 133 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?    | Done     | Done       | 0.9916720945680265 | 0      |
| 134 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 16384]> mat2 = ?     | Done     | Done       | 0.999965281197243  | 0      |
| 135 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 32]> mat2 = ?        | Done     | Done       | 0.9999674712909625 | 0      |
| 136 | Tensor<[384, 768]> self = ?,<br>Tensor<[768, 196]> mat2 = ?      | Done     | Done       | 0.9998868869153998 | 0      |
| 137 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?      | Unknown  | Done       | 0.9998842847081357 | 0      |
| 138 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?        | Unknown  | Done       | 0.9999683213479995 | 0      |
| 139 | Tensor<[4096, 197]> self = ?,<br>Tensor<[197, 1024]> mat2 = ?    | Done     | Done       | 0.9999708370049118 | 0      |
| 140 | Tensor<[4096, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?      | Done     | Done       | 0.9999752890395102 | 0      |
| 141 | Tensor<[4096, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?     | Unknown  | Done       | 0.99997408005601   | 0      |
| 142 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?       | Done     | Done       | 0.9999864505589131 | 0      |
| 143 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     | Done       | 0.9999863647893144 | 0      |
| 144 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?     | Unknown  | Done       | 0.9998871134945791 | 0      |
| 145 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.9999683883157889 | 0      |
| 146 | Tensor<[49, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ?     | Done     | Done       | 0.9999600818738357 | 0      |
| 147 | Tensor<[49, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ?    | Done     | Done       | 0.9999555359903031 | 0      |
| 148 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?     | Unknown  | Done       | 0.9999652642228085 | 0      |
| 149 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?     | Unknown  | Done       | 0.9999671895616642 | 0      |
| 150 | Tensor<[50, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Unknown  | Done       | 0.999945262325536  | 0      |
| 151 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?      | Unknown  | Done       | 0.9999684713568275 | 0      |
| 152 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.9999680689444703 | 0      |
| 153 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 2048]> mat2 = ?       | Unknown  | Done       | 0.9999943283269217 | 0      |
| 154 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?        | Unknown  | Done       | 0.9999943578663891 | 0      |
| 155 | Tensor<[512, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?          | Unknown  | Done       | 0.9999959500758963 | 0      |
| 156 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?      | Done     | Done       | 0.9999644206746261 | 0      |
| 157 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 768]> mat2 = ?      | Done     | Done       | 0.9999754435089351 | 0      |
| 158 | Tensor<[512, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?          | Unknown  | Done       | 0.999995053620725  | 0      |
| 159 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?     | Unknown  | Done       | 0.9998374431028667 | 0      |
| 160 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?      | Unknown  | Done       | 0.9999714179329592 | 0      |
| 161 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?     | Unknown  | Done       | 0.9999287578929454 | 0      |
| 162 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ?     | Done     | Done       | 0.9999599693959237 | 0      |
| 163 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?           | Done     | Done       | 0.9999957187491935 | 0      |
| 164 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?            | Done     | Done       | 0.9999938747521058 | 0      |
| 165 | Tensor<[64, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ?    | Done     | Done       | 0.9999555502014196 | 0      |
| 166 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 4096]> mat2 = ?      | Done     | Done       | 0.9999754466610125 | 0      |
| 167 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?        | Done     | Done       | 0.9999656407253446 | 0      |
| 168 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 256]> mat2 = ?     | Done     | Done       | 0.9990005242556791 | 0      |
| 169 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?      | Done     | Done       | 0.9990175465894614 | 0      |
| 170 | Tensor<[640, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?    | Done     | Done       | 0.9999655474666171 | 0      |
| 171 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ?          | Done     | Done       | 0.9999470400553169 | 0      |
| 172 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 3072]> mat2 = ?     | Done     | Done       | 0.9999707876435283 | 0      |
| 173 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ?      | Done     | Done       | 0.9999707582961676 | 0      |
| 174 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 3072]> mat2 = ?     | Done     | Done       | 0.9999708660261171 | 0      |
| 175 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?      | Done     | Done       | 0.9999706042790636 | 0      |
| 176 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 3072]> mat2 = ?       | Unknown  | Done       | 0.9999859915330233 | 0      |
| 177 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?        | Unknown  | Done       | 0.9999859716464929 | 0      |
| 178 | Tensor<[784, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?          | Done     | Done       | 0.9999954252547388 | 0      |
| 179 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?      | Done     | Done       | 0.9999728928139273 | 0      |
| 180 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?      | Done     | Done       | 0.9999712045025693 | 0      |
| 181 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 1280]> mat2 = ?       | Unknown  | Done       | 0.9999676988680045 | 0      |
| 182 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 320]> mat2 = ?        | Unknown  | Done       | 0.9998973962047994 | 0      |
| 183 | Tensor<[9, 768]> self = ?,<br>Tensor<[768, 640]> mat2 = ?        | Unknown  | Done       | 0.99996892973193   | 0      |
| 184 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?      | Done     | Done       | 0.9999752930364956 | 0      |
| 185 | Tensor<[s0*s1, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 186 | Tensor<[s0*s1, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 187 | Tensor<[s1*s2, 1280]> self = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 188 | Tensor<[s1*s2, 320]> self = ?,<br>Tensor<[320, 320]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 189 | Tensor<[s1*s2, 640]> self = ?,<br>Tensor<[640, 640]> mat2 = ?    | Unknown  | Unknown    | N/A                | N/A    |

