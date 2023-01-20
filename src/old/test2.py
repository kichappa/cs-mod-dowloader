import re

a = b'''CGSF\x03\x00
\x02\x00
\x00
\x00
\x11loadingImageIndex\x00
\x00
\x00
\x00
\x0enightPlayCount\xfd\x7f\x00
\x00
\x19\x03\x00
\x00
\x0epdx_acc_linked\x00
\x0cpdxLoginUsed\x00
\x14pdx_acc_linkPrompted\x00
.2862121823 81 Tiles 2 TESTING144545072.enabled\x00
62414618415 Adaptive Networks (AN)  V3479983473.enabled\x01
=2133705267 Advanced Building Level Control 1911986403.enabled\x01
?1394468624 Advanced Stop Selection (ex MTSE)-1650461541.enabled\x01
,563229150 Advanced Toolbar1130434717.enabled\x01
C2030755273 Automatic Pedestrian Bridge Builder V2-351728481.enabled\x01
)1627986403 Bulldoze It!-147024976.enabled\x01
-2818311563 Call Again v1.6-1662185383.enabled\x01
E2881031511 Compatibility Report v2.2.0 (Catalogue 62083866021.enabled\x01
\'845665815 CSL Map View226451794.enabled\x01
92104976832 Continues Junction median V2-312989040.enabled\x01
-821539759 Disable Zone Check681726682.enabled\x00
21689984220 Electric Roads Mod 3.0834598276.enabled\x01
L611254368 Environment Changer (+ Improved Theme Selection )243959121.enabled\x01
3502750307 Extra Landscaping Tools-772093027.enabled\x00
\'2133885971 Find It! 2-876182785.enabled\x01
82869784351 Forest Brush Revisited v1.31614001939.enabled\x01
)2105755179 FPS Booster-1321275426.enabled\x01
.2781804786 Game Anarchy 0.9-1907842962.enabled\x01
\x19HardMode359566143.enabled\x00
D2040656402 Harmony 2.2.2-0 (Mod Dependency) [1.16-1848780883.enabled\x01
82140418403 Intersection Marking Tool 1-765361785.enabled\x01
;2858591409 Loading Screen Mod Revisited 1-633452193.enabled\x01
#1619685021 Move It901300072.enabled\x01
,2862881785 Network Anarchy1609588654.enabled\x01
A2152013104 Network detective (for debuggin mods)-47040329.enabled\x01
0812125426 Network Extensions 21050807296.enabled\x01
K2730687809 Network Extensions 3 (Backup your mods now) old555699180.enabled\x00
22560782729 Network Multitool 1.31539283145.enabled\x01
72472062376 Node Controller Renewal 3.3-38504905.enabled\x01
\x1dPatchLoader-871049526.enabled\x01
2445589127 Precision Engineering-1169879199.enabled\x01
/1094334744 Procedural Objects-512470225.enabled\x01
;694512541 Prop Line Tool  [PLT]  (vAlpha)1272093498.enabled\x01
)791221322 Prop Precision587580245.enabled\x01
/556784825 Random Tree Rotation719949034.enabled\x00
\'1420955187 Real Time-1164597556.enabled\x00
(1656549865 Rebuild It!2127665977.enabled\x01
72016920607 Ploppable RICO Revisited 2.521476669.enabled\x01
/1625704117 Roundabout Builder1694258001.enabled\x00
71677913611 Smart Intersection Builder1425018038.enabled\x00
*1637663252 TM_PE 11.7.3-1374108545.enabled\x01
\'1764637396 Toggle It!-576880597.enabled\x01
%1890830956 Undo It!-120007982.enabled\x01
/2255219025 UnifiedUI (UUI) 2-1961983899.enabled\x01
 UnlimitedMoney1572287920.enabled\x00
%1783307723 Zone It!1223121438.enabled\x01
%UnlimitedOilAndOre-1335923987.enabled\x00
\x1fUnlimitedSoil-226197105.enabled\x01
\x1bUnlockAll1021273036.enabled\x00
\x05Money\x00
\x10FindItMainButton\x00
\'BuildingUnlocked[Water Treatment Plant]\x01
\x1fBuildingUnlocked[Landfill Site]\x01
"BuildingUnlocked[Combustion Plant]\x01
)BuildingUnlocked[Cloverleaf Intersection]\x01
\'BuildingUnlocked[Threeway Intersection]\x01
\x1dBuildingUnlocked[RoundaboutL]\x01
\x1dBuildingUnlocked[RoundaboutS]\x01
,BuildingUnlocked[Oneway Toll Booth Large 01]\x01
-BuildingUnlocked[Oneway Toll Booth Medium 01]\x01
,BuildingUnlocked[Twoway Toll Booth Large 01]\x01
-BuildingUnlocked[Twoway 
Toll Booth Medium 01]\x01
%BuildingUnlocked[Police Headquarters]\x01
 BuildingUnlocked[Police Station]\x01
 BuildingUnlocked[Expensive Park]\x01
&BuildingUnlocked[Expensive Playground]\x01
!BuildingUnlocked[Expensive Plaza]\x01
\x1eBuildingUnlocked[Regular Park]\x01
$BuildingUnlocked[Regular Playground]\x01
\x1fBuildingUnlocked[Regular Plaza]\x01
 BuildingUnlocked[Fishing Island]\x01
\x1fBuildingUnlocked[Floating Cafe]\x01
!BuildingUnlocked[Tropical Garden]\x01
\x1eBuildingUnlocked[Fire Station]\x01
\x1cBuildingUnlocked[Fire House]\x01
\x1cBuildingUnlocked[ExpoCenter]\x01
\x1dBuildingUnlocked[Opera House]\x01
\x1cBuildingUnlocked[Grand Mall]\x01
$BuildingUnlocked[Theater of Wonders]\x01
#BuildingUnlocked[Modern Art Museum]\x01
\x1fBuildingUnlocked[ScienceCenter]\x01
)BuildingUnlocked[Cathedral of Plentitude]\x01
!BuildingUnlocked[Transport Tower]\x01
\'BuildingUnlocked[Fountain of LifeDeath]\x01
\'BuildingUnlocked[Friendly Neighborhood]\x01
\x19BuildingUnlocked[Library]\x01
 BuildingUnlocked[StatueOfWealth]\x01
"BuildingUnlocked[Winter Market 01]\x01
\'BuildingUnlocked[Academic Library 01 A]\x01
#BuildingUnlocked[Elementary School]\x01
\x1dBuildingUnlocked[High School]\x01
\x1cBuildingUnlocked[University]\x01
\x1cBuildingUnlocked[Library 01]\x01
%BuildingUnlocked[Nuclear Power Plant]\x01
#BuildingUnlocked[Solar Power Plant]\x01
\'BuildingUnlocked[Advanced Wind Turbine]\x01
!BuildingUnlocked[Oil Power Plant]\x01
\x1bBuildingUnlocked[Bus Depot]\x01
\x1fBuildingUnlocked[Train Station]\x01
\x19BuildingUnlocked[Airport]\x01
\x18BuildingUnlocked[Harbor]\x01
\x1eBuildingUnlocked[Cargo Center]\x01
\x1eBuildingUnlocked[Cargo Harbor]\x01
 BuildingUnlocked[Metro Entrance]\x01
-BuildingUnlocked[Overground 
Metro Station 01]\x01
6BuildingUnlocked[Overground Metro Station Elevated 01]\x01
.BuildingUnlocked[ChirpyBirthday Balloon Tours]\x01
 BuildingUnlocked[Medical Clinic]\x01
\x1aBuildingUnlocked[Hospital]\x01
\x1bBuildingUnlocked[Crematory]\x01
\x1aBuildingUnlocked[Cemetery]\x01
\x1eBuildingUnlocked[Eldercare 01]\x01
(BuildingUnlocked[Child Health Center 01]\x01
\x1eBuildingUnlocked[MerryGoRound]\x01
 BuildingUnlocked[bouncer_castle]\x01
"BuildingUnlocked[Basketball Court]\x01
"BuildingUnlocked[Botanical garden]\x01
 BuildingUnlocked[dog-park-fence]\x01
 BuildingUnlocked[JapaneseGarden]\x01
"BuildingUnlocked[Brandenburg Gate]\x01
\x1dBuildingUnlocked[MagickaPark]\x01
\x1fBuildingUnlocked[Large Airport]\x01
\x1cBuildingUnlocked[Taxi Depot]\x01
\x1bBuildingUnlocked[Cargo Hub]\x01
\x1dBuildingUnlocked[Bus Station]\x01
\x18BuildingUnlocked[Prison]\x01
$BuildingUnlocked[2x2_Jet_ski_rental]\x01
!BuildingUnlocked[2x8_FishingPier]\x01
#BuildingUnlocked[3x2_Fishing tours]\x01
\x1cBuildingUnlocked[4x4_Marina]\x01
#BuildingUnlocked[9x15_RidingStable]\x01
\x1bBuildingUnlocked[Skatepark]\x01
#BuildingUnlocked[Beachvolley Court]\x01
$BuildingUnlocked[2x4_RestaurantPier]\x01
\x1cBuildingUnlocked[Tram Depot]\x01
"BuildingUnlocked[Geothermal_Plant]\x01
\x17BuildingUnlocked[Sauna]\x01
 BuildingUnlocked[Boiler Station]\x01
(BuildingUnlocked[Road Maintenance Depot]\x01
(BuildingUnlocked[Police Helicopter Base]\x01
)BuildingUnlocked[Medical Helicopter Base]\x01
&BuildingUnlocked[Fire Helicopter Base]\x01
)BuildingUnlocked[Small Emergency Shelter]\x01
)BuildingUnlocked[Large Emergency Shelter]\x01
"BuildingUnlocked[Radio Mast Short]\x01
!BuildingUnlocked[Radio Mast Tall]\x01
!BuildingUnlocked[Firewatch Tower]\x01
\x1fBuildingUnlocked[Weather Radar]\x01
1BuildingUnlocked[Disaster Response Unit Backyard]\x01
(BuildingUnlocked[Disaster Response Unit]\x01
0BuildingUnlocked[Water Pumping Service Building]\x01
!BuildingUnlocked[Water Reservoir]\x01
$BuildingUnlocked[Fresh Water Outlet]\x01
"BuildingUnlocked[Deep Space Radar]\x01
&BuildingUnlocked[Tsunami Warning Buoy]\x01
1BuildingUnlocked[Earthquake Early Warning Sensor]\x01
!BuildingUnlocked[Helicopter Park]\x01
$BuildingUnlocked[Large Trainstation]\x01
\x1dBuildingUnlocked[Blimp Depot]\x01
\x1cBuildingUnlocked[Blimp Stop]\x01
\x1fBuildingUnlocked[Ferry Bus Hub]\x01
\x1eBuildingUnlocked[Ferry Harbor]\x01
\x1cBuildingUnlocked[Ferry Pier]\x01
\x1dBuildingUnlocked[Ferry Depot]\x01
.BuildingUnlocked[End of the line Trainstation]\x01
\x1dBuildingUnlocked[Boat Museum]\x01
\'BuildingUnlocked[Cable Car Station End]\x01
 BuildingUnlocked[Cable Car Stop]\x01
\x1eBuildingUnlocked[Traffic Park]\x01
-BuildingUnlocked[Monorail Station Standalone]\x01
)BuildingUnlocked[Monorail Station Avenue]\x01
"BuildingUnlocked[Monorail Bus Hub]\x01
*BuildingUnlocked[Monorail Train Metro Hub]\x01
(BuildingUnlocked[Boat Museum Steam Boat]\x01
#BuildingUnlocked[Lungs of the City]\x01
%BuildingUnlocked[Solar Updraft Tower]\x01
"BuildingUnlocked[Recycling Center]\x01
-BuildingUnlocked[Modern Technology Institute]\x01
7BuildingUnlocked[Ocean Thermal Energy Conversion Plant]\x01
(BuildingUnlocked[Geothermal Power Plant]\x01
+BuildingUnlocked[Sports Hall and Gymnasium]\x01
!BuildingUnlocked[Ziggurat Garden]\x01
\x1eBuildingUnlocked[Central Park]\x01
,BuildingUnlocked[Floating Garbage Collector]\x01
"BuildingUnlocked[Community School]\x01
#BuildingUnlocked[Biofuel Bus Depot]\x01
-BuildingUnlocked[University of Creative Arts]\x01
+BuildingUnlocked[Eco Water Treatment Plant]\x01
 BuildingUnlocked[Community Pool]\x01
\x1dBuildingUnlocked[Yoga Garden]\x01
\x1eBuildingUnlocked[Sea Fortress]\x01
*BuildingUnlocked[The Statue Of Colossalus]\x01
#BuildingUnlocked[Sealife Enclosure]\x01
*BuildingUnlocked[Sealife Enclosure Sub 01]\x01
*BuildingUnlocked[Sealife Enclosure Sub 02]\x01
$BuildingUnlocked[Bouldering Site 01]\x01
!BuildingUnlocked[Camping Site 01]\x01
%BuildingUnlocked[Park Chess Board 01]\x01
0BuildingUnlocked[Insect Amphibian Reptile House]\x01
*BuildingUnlocked[Nature Reserve Main Gate]\x01
.BuildingUnlocked[Moose And Reindeer Enclosure]\x01
*BuildingUnlocked[Nature Reserve Side Gate]\x01
*BuildingUnlocked[Amusement Park Main Gate]\x01
*BuildingUnlocked[Amusement Park Side Gate]\x01
&BuildingUnlocked[Tent Camping Site 01]\x01
\x19BuildingUnlocked[Tent 03]\x01
\x19BuildingUnlocked[Tent 02]\x01
\x19BuildingUnlocked[Tent 01]\x01
\x1fBuildingUnlocked[Zoo Main Gate]\x01
"BuildingUnlocked[Fishing Cabin 01]\x01
\x1fBuildingUnlocked[Zoo Side Gate]\x01
"BuildingUnlocked[Fishing Cabin 02]\x01
"BuildingUnlocked[Lookout Tower 01]\x01
"BuildingUnlocked[Lookout Tower 02]\x01
&BuildingUnlocked[Zoo Souvenir Shop 01]\x01
1BuildingUnlocked[Amusement Park Souvenir Shop 01]\x01
\x1fBuildingUnlocked[Rollercoaster]\x01
-BuildingUnlocked[Amusement Park Restrooms 01]\x01
\'BuildingUnlocked[Sightseeing Bus Depot]\x01
"BuildingUnlocked[Hunting Cabin 01]\x01
"BuildingUnlocked[Hunting Cabin 02]\x01
$BuildingUnlocked[Lean-To Shelter 01]\x01
$BuildingUnlocked[Lean-To Shelter 02]\x01
\'BuildingUnlocked[Hot Air Balloon Tours]\x01
!BuildingUnlocked[Drop Tower Ride]\x01
"BuildingUnlocked[Campfire Site 01]\x01
"BuildingUnlocked[Campfire Site 02]\x01
\x1fBuildingUnlocked[Pendulum Ride]\x01
\x1eBuildingUnlocked[Ferris Wheel]\x01
+BuildingUnlocked[Park Maintenance Building]\x01
!BuildingUnlocked[Viewing Deck 01]\x01
!BuildingUnlocked[Viewing Deck 02]\x01
$BuildingUnlocked[Antelope Enclosure]\x01
 BuildingUnlocked[Park Main Gate]\x01
!BuildingUnlocked[Bison Enclosure]\x01
\x1fBuildingUnlocked[Swinging Boat]\x01
$BuildingUnlocked[Trampoline Park 01]\x01
 BuildingUnlocked[Park Side Gate]\x01
#BuildingUnlocked[Rotating Tea Cups]\x01
\x1cBuildingUnlocked[Park Plaza]\x01
"BuildingUnlocked[House Of Horrors]\x01
$BuildingUnlocked[Park Info Booth 01]\x01
\x1bBuildingUnlocked[City Arch]\x01
\x1fBuildingUnlocked[Game Booth 01]\x01
\x1fBuildingUnlocked[Game Booth 02]\x01
\x1dBuildingUnlocked[Bumper Cars]\x01
\x1bBuildingUnlocked[Gazebo 01]\x01
\x1dBuildingUnlocked[Piggy Train]\x01
\x1bBuildingUnlocked[Gazebo 02]\x01
"BuildingUnlocked[Zoo Restrooms 01]\x01
\x1eBuildingUnlocked[Park Pier 01]\x01
$BuildingUnlocked[Flamingo Enclosure]\x01
\x1eBuildingUnlocked[Park Pier 02]\x01
#BuildingUnlocked[Climbing Frame 01]\x01
#BuildingUnlocked[Park Restrooms 01]\x01
\x1fBuildingUnlocked[Monkey Palace]\x01
!BuildingUnlocked[Rhino Enclosure]\x01
\x1cBuildingUnlocked[Bird House]\x01
\x1dBuildingUnlocked[Zoo Cafe 01]\x01
$BuildingUnlocked[Elephant Enclosure]\x01
\x1eBuildingUnlocked[Zoo Plaza 01]\x01
\x1eBuildingUnlocked[Park Cafe 01]\x01
#BuildingUnlocked[Giraffe Enclosure]\x01
#BuildingUnlocked[Observation Tower]\x01
\x1aBuildingUnlocked[Carousel]\x01
(BuildingUnlocked[Amusement Park Cafe 01]\x01
 BuildingUnlocked[Lion Enclosure]\x01
)BuildingUnlocked[Amusement Park Plaza 01]\x01
&BuildingUnlocked[Small Park Main Gate]\x01
0BuildingUnlocked[Small Nature Reserve Main Gate]\x01
%BuildingUnlocked[Small Zoo Main Gate]\x01
0BuildingUnlocked[Small Amusement Park Main Gate]\x01
 BuildingUnlocked[Post Office 01]\x01
*BuildingUnlocked[Post Sorting Facility 01]\x01
\x1fBuildingUnlocked[Grain Silo 01]\x01
"BuildingUnlocked[Cargo Airport 01]\x01
\x1fBuildingUnlocked[Grain Silo 02]\x01
&BuildingUnlocked[Cargo Airport Hub 01]\x01
#BuildingUnlocked[Warehouse Yard 01]\x01
$BuildingUnlocked[Small Warehouse 01]\x01
%BuildingUnlocked[Medium Warehouse 01]\x01
$BuildingUnlocked[Large Warehouse 01]\x01
\x1fBuildingUnlocked[Flour Mill 01]\x01
3BuildingUnlocked[Offshore Oil Drilling Platform 01]\x01
,BuildingUnlocked[Farm Main Building Level 1]\x01
\x1dBuildingUnlocked[Saw Mill 01]\x01
\x1bBuildingUnlocked[Bakery 01]\x01
*BuildingUnlocked[Engineered Wood Plant 01]\x01
*BuildingUnlocked[Tree Plantation Alder 01]\x01
*BuildingUnlocked[Tree Plantation Beech 01]\x01
,BuildingUnlocked[Tree Plantation Conifer 01]\x01
\x1dBuildingUnlocked[Ore Mine 01]\x01
#BuildingUnlocked[Animal Pasture 01]\x01
#BuildingUnlocked[Animal Pasture 02]\x01
0BuildingUnlocked[Animal Pasture 01 Highland Cow]\x01
0BuildingUnlocked[Animal Pasture 02 Highland Cow]\x01
\'BuildingUnlocked[Animal Pasture 01 Pig]\x01
\'BuildingUnlocked[Animal Pasture 02 Pig]\x01
)BuildingUnlocked[Animal Pasture 01 Sheep]\x01
)BuildingUnlocked[Animal Pasture 02 Sheep]\x01
\x1dBuildingUnlocked[Oil Pump 01]\x01
\x1dBuildingUnlocked[Oil Pump 02]\x01
)BuildingUnlocked[Biomass Pellet Plant 01]\x01
4BuildingUnlocked[Ore Industry Main Building Level 1]\x01
/BuildingUnlocked[Oil Sludge Pyrolysis Plant 01]\x01
-BuildingUnlocked[Waste Oil Refining Plant 01]\x01
2BuildingUnlocked[Ore Industry Workers Barracks 01]\x01
\x1eBuildingUnlocked[Pulp Mill 01]\x01
(BuildingUnlocked[Petrochemical Plant 01]\x01
0BuildingUnlocked[Forestry Main Building Level 1]\x01
%BuildingUnlocked[Oil Drilling Rig 01]\x01
%BuildingUnlocked[Oil Drilling Rig 02]\x01
&BuildingUnlocked[Rotary Kiln Plant 01]\x01
%BuildingUnlocked[Lemonade Factory 01]\x01
!BuildingUnlocked[Food Factory 01]\x01
%BuildingUnlocked[Clothing Factory 01]\x01
4BuildingUnlocked[Oil Industry Main Building Level 1]\x01
*BuildingUnlocked[Naphtha Cracker Plant 01]\x01
*BuildingUnlocked[Farm Workers Barracks 01]\x01
 BuildingUnlocked[Car Factory 01]\x01
&BuildingUnlocked[Furniture Factory 01]\x01
.BuildingUnlocked[Household Plastic Factory 01]\x01
*BuildingUnlocked[Modular House Factory 01]\x01
#BuildingUnlocked[Printing Press 01]\x01
$BuildingUnlocked[Sneaker Factory 01]\x01
\'BuildingUnlocked[Soft Paper 
Factory 01]\x01
 BuildingUnlocked[Toy Factory 01]\x01
(BuildingUnlocked[Electronics Factory 01]\x01
+BuildingUnlocked[Industrial Steel Plant 01]\x01
6BuildingUnlocked[Oil Industry Maintenance Building 01]\x01
2BuildingUnlocked[Oil Industry Workers Barracks 01]\x01
%BuildingUnlocked[Saw Dust Storage 01]\x01
.BuildingUnlocked[Forestry Workers Barracks 01]\x01
(BuildingUnlocked[Crude Oil Tank Farm 01]\x01
(BuildingUnlocked[Crude Oil Tank Farm 02]\x01
6BuildingUnlocked[Ore Industry Maintenance Building 01]\x01
&BuildingUnlocked[Wood Chip Storage 01]\x01
%BuildingUnlocked[Fiberglass Plant 01]\x01
.BuildingUnlocked[Glass Manufacturing Plant 01]\x01
 BuildingUnlocked[Ore Storage 01]\x01
!BuildingUnlocked[Sand Storage 01]\x01
-BuildingUnlocked[Crude Oil Storage Cavern 01]\x01
2BuildingUnlocked[Forestry Maintenance Building 01]\x01
$BuildingUnlocked[Milking Parlour 01]\x01
.BuildingUnlocked[Farm Maintenance Building 01]\x01
)BuildingUnlocked[Ore Industry Storage 01]\x01
\'BuildingUnlocked[Petroleum Refinery 01]\x01
 BuildingUnlocked[Cattle Shed 01]\x01
(BuildingUnlocked[Raw Mineral Storage 01]\x01
,BuildingUnlocked[Tree Plantation Conifer 02]\x01
3BuildingUnlocked[Tree Plantation Conifer 02 Sub 01]\x01
*BuildingUnlocked[Tree Plantation Alder 02]\x01
1BuildingUnlocked[Tree Plantation Alder 02 Sub 01]\x01
*BuildingUnlocked[Tree Plantation Beech 02]\x01
1BuildingUnlocked[Tree Plantation Beech 02 Sub 01]\x01
\x19BuildingUnlocked[Barn 01]\x01
\x19BuildingUnlocked[Barn 02]\x01
$BuildingUnlocked[Slaughter House 01]\x01
)BuildingUnlocked[Oil Industry Storage 01]\x01
*BuildingUnlocked[Tree Plantation Alder 03]\x01
,BuildingUnlocked[Tree Plantation Conifer 03]\x01
*BuildingUnlocked[Tree Plantation Beech 03]\x01
1BuildingUnlocked[Tree Plantation Beech 03 Sub 01]\x01
1BuildingUnlocked[Tree Plantation Beech 03 Sub 02]\x01
1BuildingUnlocked[Tree Plantation Beech 03 Sub 03]\x01
1BuildingUnlocked[Tree Plantation Alder 03 Sub 01]\x01
1BuildingUnlocked[Tree Plantation Alder 03 Sub 02]\x01
3BuildingUnlocked[Tree Plantation Conifer 03 Sub 01]\x01
3BuildingUnlocked[Tree Plantation Conifer 03 Sub 02]\x01
3BuildingUnlocked[Tree Plantation Conifer 03 Sub 03]\x01
3BuildingUnlocked[Tree Plantation Conifer 03 Sub 04]\x01
\x1dBuildingUnlocked[Log Yard 01]\x01
\x1dBuildingUnlocked[Log Yard 02]\x01
)BuildingUnlocked[Seabed Mining Vessel 01]\x01
&BuildingUnlocked[Ore Grinding Mill 01]\x01
)BuildingUnlocked[Ore Mine Underground 01]\x01
)BuildingUnlocked[Ore Mine Underground 02]\x01
\x1dBuildingUnlocked[Ore Mine 03]\x01
\x1dBuildingUnlocked[Dry Dock 01]\x01
\x1dBuildingUnlocked[Ore Mine 02]\x01
\'BuildingUnlocked[Tree Sapling Field 01]\x01
\'BuildingUnlocked[Tree Sapling Field 02]\x01
-BuildingUnlocked[Tree Sapling Green House 01]\x01
-BuildingUnlocked[Tree Sapling Green House 02]\x01
$BuildingUnlocked[Crop Field Corn 01]\x01
$BuildingUnlocked[Crop Field Corn 02]\x01
$BuildingUnlocked[Crop Field Corn 03]\x01
&BuildingUnlocked[Crop Field Cotton 01]\x01
&BuildingUnlocked[Crop Field Cotton 02]\x01
&BuildingUnlocked[Crop Field Cotton 03]\x01
&BuildingUnlocked[Crop Field Potato 01]\x01
&BuildingUnlocked[Crop Field Potato 02]\x01
&BuildingUnlocked[Crop Field Potato 03]\x01
%BuildingUnlocked[Crop Field Wheat 01]\x01
%BuildingUnlocked[Crop Field Wheat 02]\x01
%BuildingUnlocked[Crop Field Wheat 03]\x01
&BuildingUnlocked[Fruit Field Apple 01]\x01
&BuildingUnlocked[Fruit Field Apple 02]\x01
&BuildingUnlocked[Fruit Field Apple 03]\x01
\'BuildingUnlocked[Fruit Field Orange 01]\x01
\'BuildingUnlocked[Fruit Field Orange 02]\x01
\'BuildingUnlocked[Fruit Field Orange 03]\x01
%BuildingUnlocked[Fruit Field Pear 01]\x01
%BuildingUnlocked[Fruit Field Pear 02]\x01
%BuildingUnlocked[Fruit Field Pear 03]\x01
+BuildingUnlocked[Crop Field Green House 01]\x01
+BuildingUnlocked[Crop Field Green House 02]\x01
+BuildingUnlocked[Crop Field Green House 03]\x01
,BuildingUnlocked[Fruit Field Green House 01]\x01
,BuildingUnlocked[Fruit Field Green House 02]\x01
,BuildingUnlocked[Fruit Field Green House 03]\x01
0BuildingUnlocked[Trade School Administration 01]\x01
+BuildingUnlocked[Trade School Dormitory 01]\x01
.BuildingUnlocked[American Football Stadium 01]\x01
*BuildingUnlocked[School of Engineering 01]\x01
1BuildingUnlocked[Trade School Academic Statue 01]\x01
1BuildingUnlocked[Trade 
School Academic Statue 02]\x01
,BuildingUnlocked[Trade School Auditorium 01]\x01
+BuildingUnlocked[Trade School Book Club 01]\x01
+BuildingUnlocked[Trade School Bookstore 01]\x01
+BuildingUnlocked[Trade School Cafeteria 01]\x01
*BuildingUnlocked[Trade School Fountain 01]\x01
0BuildingUnlocked[Trade School Groundskeeping 01]\x01
+BuildingUnlocked[Trade School Gymnasium 01]\x01
)BuildingUnlocked[Trade School IT Club 01]\x01
.BuildingUnlocked[Trade School Laboratories 01]\x01
)BuildingUnlocked[Trade School Library 01]\x01
+BuildingUnlocked[Trade School Media Lab 01]\x01
,BuildingUnlocked[Trade School Study Hall 01]\x01
1BuildingUnlocked[Liberal Arts Academic Statue 01]\x01
1BuildingUnlocked[Liberal Arts Academic Statue 02]\x01
*BuildingUnlocked[Liberal Arts Art Club 01]\x01
,BuildingUnlocked[Liberal Arts Auditorium 01]\x01
+BuildingUnlocked[Liberal Arts Bookstore 01]\x01
+BuildingUnlocked[Liberal Arts Cafeteria 01]\x01
,BuildingUnlocked[Liberal Arts Dance Club 01]\x01
+BuildingUnlocked[Liberal Arts Dormitory 01]\x01
,BuildingUnlocked[Liberal Arts Drama Club 01]\x01
*BuildingUnlocked[Liberal Arts Fountain 01]\x01
0BuildingUnlocked[Liberal Arts Groundskeeping 01]\x01
+BuildingUnlocked[Liberal Arts Gymnasium 01]\x01
.BuildingUnlocked[Liberal Arts Laboratories 01]\x01
)BuildingUnlocked[Liberal Arts Library 01]\x01
+BuildingUnlocked[Liberal Arts Media Lab 01]\x01
,BuildingUnlocked[Liberal Arts Study Hall 01]\x01
/BuildingUnlocked[University Academic Statue 01]\x01
/BuildingUnlocked[University Academic Statue 02]\x01
*BuildingUnlocked[University Auditorium 01]\x01
)BuildingUnlocked[University Bookstore 01]\x01
)BuildingUnlocked[University Cafeteria 01]\x01
*BuildingUnlocked[University Chess Club 01]\x01
)BuildingUnlocked[University Dormitory 01]\x01
(BuildingUnlocked[University Fountain 01]\x01
.BuildingUnlocked[University Groundskeeping 01]\x01
)BuildingUnlocked[University Gymnasium 01]\x01
,BuildingUnlocked[University Laboratories 01]\x01
\'BuildingUnlocked[University Library 01]\x01
)BuildingUnlocked[University Math Club 01]\x01
)BuildingUnlocked[University Media Lab 01]\x01
+BuildingUnlocked[University Soccer Club 01]\x01
*BuildingUnlocked[University Study Hall 01]\x01
(BuildingUnlocked[School of Economics 01]\x01
(BuildingUnlocked[School of Education 01]\x01
4BuildingUnlocked[School of Environmental Studies 01]\x01
#BuildingUnlocked[Police Academy 01]\x01
1BuildingUnlocked[School of Tourism And Travel 01]\x01
"BuildingUnlocked[School of Law 01]\x01
\'BuildingUnlocked[School of Medicine 01]\x01
&BuildingUnlocked[School of Science 01]\x01
.BuildingUnlocked[University Administration 01]\x01
0BuildingUnlocked[Liberal Arts Administration 01]\x01
\'BuildingUnlocked[Baseball Park 01 Main]\x01
(BuildingUnlocked[Liberal Arts Museum 01]\x01
(BuildingUnlocked[Trade School Museum 01]\x01
&BuildingUnlocked[University Museum 01]\x01
/BuildingUnlocked[Liberal Arts Outdoor Study 01]\x01
/BuildingUnlocked[Trade School Outdoor Study 01]\x01
-BuildingUnlocked[University Outdoor Study 01]\x01
%BuildingUnlocked[Basketball Arena 01]\x01
$BuildingUnlocked[Aquatics Center 01]\x01
,BuildingUnlocked[Track And Field Stadium 01]\x01
5BuildingUnlocked[Liberal Arts Commencement Office 01]\x01
5BuildingUnlocked[Trade School Commencement Office 01]\x01
3BuildingUnlocked[University Commencement Office 01]\x01
7BuildingUnlocked[Trade School Beach Volleyball Club 01]\x01
,BuildingUnlocked[Waste Transfer Facility 01]\x01
-BuildingUnlocked[Waste Processing Complex 01]\x01
,BuildingUnlocked[Passenger Helicopter Depot]\x01
+BuildingUnlocked[Passenger Helicopter Stop]\x01
:BuildingUnlocked[Advanced Inland Water Treatment Plant 01]\x01
&BuildingUnlocked[Large Water Tower 01]\x01
%BuildingUnlocked[Trolleybus Depot 01]\x01
$BuildingUnlocked[Transport Hub 03 A]\x01
\x1eBuildingUnlocked[Fish Farm 01]\x01
!BuildingUnlocked[Fish Factory 01]\x01
*BuildingUnlocked[Intercity Bus Station 01]\x01
*BuildingUnlocked[Intercity Bus Station 02]\x01
(BuildingUnlocked[Fishing Boat Harbor 01]\x01
"BuildingUnlocked[Fish Farm 01 Sub]\x01
$BuildingUnlocked[Aviation Club 01 A]\x01
$BuildingUnlocked[Aviation Club 01 B]\x01
$BuildingUnlocked[Aviation Club 01 C]\x01
$BuildingUnlocked[Transport Hub 01 A]\x01
$BuildingUnlocked[Transport Hub 02 A]\x01
 BuildingUnlocked[Fish Market 
01]\x01
\x1eBuildingUnlocked[Fish Farm 02]\x01
"BuildingUnlocked[Fish Farm 02 Sub]\x01
\x1eBuildingUnlocked[Fish Farm 03]\x01
"BuildingUnlocked[Fish Farm 03 Sub]\x01
(BuildingUnlocked[Fishing Boat Harbor 02]\x01
(BuildingUnlocked[Fishing Boat Harbor 03]\x01
(BuildingUnlocked[Fishing Boat Harbor 04]\x01
(BuildingUnlocked[Fishing Boat Harbor 05]\x01
$BuildingUnlocked[Transport Hub 04 E]\x01
$BuildingUnlocked[Transport Hub 04 B]\x01
$BuildingUnlocked[Transport Hub 04 C]\x01
$BuildingUnlocked[Transport Hub 04 D]\x01
$BuildingUnlocked[Transport Hub 04 A]\x01
$BuildingUnlocked[Transport Hub 04 F]\x01
$BuildingUnlocked[Transport Hub 04 G]\x01
$BuildingUnlocked[Transport Hub 05 A]\x01
>BuildingUnlocked[Eco Advanced Inland Water Treatment Plant 01]\x01
(BuildingUnlocked[Fish Farm 02 Sub Algae]\x01
/BuildingUnlocked[Waste Processing Complex 01 B]\x01
.BuildingUnlocked[Waste Transfer Facility 01 B]\x01
\x1eBuildingUnlocked[Large Hangar]\x01
\x1eBuildingUnlocked[Small Hangar]\x01
"BuildingUnlocked[Airport Hotel 02]\x01
$BuildingUnlocked[Aviation Museum 01]\x01
(BuildingUnlocked[Large Terminal Style A]\x01
*BuildingUnlocked[Concourse Hub 01 
Style A]\x01
(BuildingUnlocked[Large Terminal Style B]\x01
*BuildingUnlocked[Concourse Hub 02 Style B]\x01
(BuildingUnlocked[Small Terminal Style B]\x01
\'BuildingUnlocked[Control Tower Style B]\x01
0BuildingUnlocked[Airport Metro Station Elevated]\x01
"BuildingUnlocked[Airport Hotel 01]\x01
\'BuildingUnlocked[Aviation Fuel Station]\x01
.BuildingUnlocked[Decoration Cargo Airplane 02]\x01
.BuildingUnlocked[Decoration Cargo Airplane 03]\x01
.BuildingUnlocked[Decoration Large Airplane 01]\x01
.BuildingUnlocked[Decoration Large Airplane 02]\x01
/BuildingUnlocked[Decoration Medium Airplane 01]\x01
/BuildingUnlocked[Decoration Medium Airplane 02]\x01
/BuildingUnlocked[Decoration Medium Airplane 03]\x01
.BuildingUnlocked[Decoration Small Airplane 01]\x01
.BuildingUnlocked[Decoration Small Airplane 02]\x01
.BuildingUnlocked[Decoration Small Airplane 03]\x01
\'BuildingUnlocked[Airport Train Station]\x01
)BuildingUnlocked[Airline Lounge Building]\x01
(BuildingUnlocked[Cargo Airport Terminal]\x01
*BuildingUnlocked[Concourse Hub 03 Style C]\x01
\'BuildingUnlocked[Control Tower Style A]\x01
\'BuildingUnlocked[Control Tower Style C]\x01
(BuildingUnlocked[Large Terminal Style C]\x01
0BuildingUnlocked[Small 2 Story Terminal Style A]\x01
(BuildingUnlocked[Small Terminal Style C]\x01
-BuildingUnlocked[Large Entrance Style B sub1]\x01
-BuildingUnlocked[Large Entrance Style B sub2]\x01
(BuildingUnlocked[Airport Bus Station 01]\x01
2BuildingUnlocked[Small Terminal One Story Style A]\x01
2BuildingUnlocked[Small Terminal One Story Style B]\x01
2BuildingUnlocked[Small Terminal One Story Style C]\x01
\x1cBuildingUnlocked[Airline HQ]\x01
%BuildingUnlocked[large_stand_01_anim]\x01
&BuildingUnlocked[medium_stand_01_anim]\x01
%BuildingUnlocked[small_stand_01_anim]\x01
4BuildingUnlocked[cargo_airport_trainstation_01_anim]\x01
%BuildingUnlocked[cargo_stand_01_anim]\x01
(BuildingUnlocked[Elevated Metro Station]\x01
\'BuildingUnlocked[High Density Hospital]\x01
-BuildingUnlocked[High Density Police 
Station]\x01
+BuildingUnlocked[High Density Fire Station]\x01
*BuildingUnlocked[High Density High School]\x01
)BuildingUnlocked[High Density University]\x01
(BuildingUnlocked[Elevated Train Station]\x01
-BuildingUnlocked[Small Pedestrian Area Plaza]\x01
%BuildingUnlocked[Food Truck Plaza 01]\x01
%BuildingUnlocked[Food Truck Plaza 02]\x01
*BuildingUnlocked[Ice Cream Stand Plaza 01]\x01
*BuildingUnlocked[Ice Cream Stand Plaza 02]\x01
!BuildingUnlocked[Statue Plaza 01]\x01
0BuildingUnlocked[High Density Elementary School]\x01
-BuildingUnlocked[High Density Metro Entrance]\x01
,BuildingUnlocked[High Density Metro Station]\x01
*BuildingUnlocked[High Density Bus Station]\x01
&BuildingUnlocked[Small Fountain Plaza]\x01
(BuildingUnlocked[Stock Exchange Level 1]\x01
"BuildingUnlocked[Football Stadium]\x01
&BuildingUnlocked[Football Stadium ITA]\x01
&BuildingUnlocked[Football Stadium ENG]\x01
&BuildingUnlocked[Football Stadium ESP]\x01
%BuildingUnlocked[Football Stadium FR]\x01
!BuildingUnlocked[Panda Sanctuary]\x01
\x18BuildingUnlocked[Temple]\x01
&BuildingUnlocked[Oriental Pearl Tower]\x01
!BuildingUnlocked[Festival Area 1]\x01
&BuildingUnlocked[Broadcasting Studios]\x01
\x19BuildingUnlocked[Biodome]\x01
"BuildingUnlocked[Cryopreservatory]\x01
\x19BuildingUnlocked[Faculty]\x01
%BuildingUnlocked[Intelligence Agency]\x01
$BuildingUnlocked[Medical Laboratory]\x01
\x1fBuildingUnlocked[Vertical Farm]\x01
"BuildingUnlocked[Wave Power Plant]\x01
)BuildingUnlocked[PDX01_driveinn_taiheiyo]\x01
\'BuildingUnlocked[PDX02_driveinn_natori]\x01
\'BuildingUnlocked[PDX03_Soba Restaurant]\x01
!BuildingUnlocked[PDX04_Udon Shop]\x01
"BuildingUnlocked[PDX05_Ramen Shop]\x01
&BuildingUnlocked[PDX06_Driveinn Large]\x01
$BuildingUnlocked[PDX07_Cityoffice_M]\x01
$BuildingUnlocked[PDX08_Cityoffice_L]\x01
%BuildingUnlocked[PDX09_medium_office]\x01
\x1fBuildingUnlocked[PDX10_JA_BLDG]\x01
#BuildingUnlocked[PDX11_Hotel_kikyo]\x01
!BuildingUnlocked[PDX12_CityHotel]\x01
%BuildingUnlocked[PDX13_Hiroshima_sta]\x01
(BuildingUnlocked[PDX14_Shizuoka_Station]\x01
\'BuildingUnlocked[PDX15_sasaki_hospital]\x01
*BuildingUnlocked[PDX16_incineration_plant]\x01
)BuildingUnlocked[PDX17_Five Story Pagora]\x01
%BuildingUnlocked[PDX18_Shinjuku_bldg]\x01
%BuildingUnlocked[PDX19_Yokohama-bldg]\x01
!BuildingUnlocked[PDX20_Shin-maru]\x01
\x19BuildingUnlocked[H_Hub01]\x01
\x1eBuildingUnlocked[H_Hub01 sub2]\x01
\x1bBuildingUnlocked[H_Hub02_A]\x01
\x19BuildingUnlocked[H_Hub03]\x01
\x1eBuildingUnlocked[H_Hub03 sub1]\x01
\x19BuildingUnlocked[H_Hub04]\x01
\x1eBuildingUnlocked[H_Hub04 sub1]\x01
1BuildingUnlocked[M_Elevated Metro Station Bypass]\x01
6BuildingUnlocked[M_Elevated Metro Station Dual Island]\x01
1BuildingUnlocked[M_Elevated Metro Station Island]\x01
(BuildingUnlocked[M_Metro Bypass Station]\x01
-BuildingUnlocked[M_Metro Dual Island Station]\x01
(BuildingUnlocked[M_Metro Island Station]\x01
1BuildingUnlocked[T_Elevated Bypass Train Station]\x01
6BuildingUnlocked[T_Elevated Bypass Train Station Sub1]\x01
6BuildingUnlocked[T_Elevated Dual Island Train Station]\x01
;BuildingUnlocked[T_Elevated Dual Island Train Station Sub1]\x01
1BuildingUnlocked[T_Elevated Island Train Station]\x01
1BuildingUnlocked[T_Elevated Island Platform Sub1]\x01
/BuildingUnlocked[T_Ground Bypass Train Station]\x01
4BuildingUnlocked[T_Ground Bypass Train Station Sub2]\x01
4BuildingUnlocked[T_Ground Dual Island Train Station]\x01
9BuildingUnlocked[T_Ground Dual Island Train Station sub1]\x01
/BuildingUnlocked[T_Ground Island Train Station]\x01
!BuildingUnlocked[ccp8-pier-seine]\x01
!BuildingUnlocked[ccp8-pier-rhine]\x01
+BuildingUnlocked[Crematorium Memorial Park]\x01
0BuildingUnlocked[Eco-Friendly Incinerator Plant]\x01
$BuildingUnlocked[Fire Safety Center]\x01
)BuildingUnlocked[Large Elementary School]\x01
(BuildingUnlocked[Mirae Department Store]\x01
(BuildingUnlocked[Plastic Surgery Center]\x01
(BuildingUnlocked[Police Security Center]\x01
\x1bBuildingUnlocked[KR C2 4x3]\x01
\x1bBuildingUnlocked[KR C2 4x4]\x01
;BuildingUnlocked[1183644172.2 Platforms Cross Station_Data]\x01
>BuildingUnlocked[1184595191.2 Platforms Parallel Station_Data]\x01
BBuildingUnlocked[1185164524.2 Platforms Parallel Various Lvl_Data]\x01
BBuildingUnlocked[1189750200.2 Platforms Double Layer Station_Data]\x01
ABuildingUnlocked[1192424132.2 Platforms Parallel Station SE_Data]\x01
.BuildingUnlocked[ChirpX Launch Control Center]\x01
\x1eBuildingUnlocked[Eden Project]\x01
#BuildingUnlocked[Oppression Office]\x01
#BuildingUnlocked[SeaAndSky Scraper]\x01
%BuildingUnlocked[High Interest Tower]\x01
\x1cBuildingUnlocked[Trash Mall]\x01
$BuildingUnlocked[Statue of Shopping]\x01
\x1bBuildingUnlocked[Posh Mall]\x01
\x1aBuildingUnlocked[SeaWorld]\x01
#BuildingUnlocked[Plaza of the Dead]\x01
\x1dBuildingUnlocked[Observatory]\x01
\x1fBuildingUnlocked[Business Park]\x01
$BuildingUnlocked[Servicing Services]\x01
\x1bBuildingUnlocked[City Hall]\x01
\x1dBuildingUnlocked[Court House]\x01
"BuildingUnlocked[Colossal Offices]\x01
\x1fBuildingUnlocked[Lazaret Plaza]\x01
\x1fBuildingUnlocked[Official Park]\x01
\x19BuildingUnlocked[Stadium]\x01
$BuildingUnlocked[Statue of Industry]\x01
%BuildingUnlocked[Academic Library 01]\x01
!BuildingUnlocked[Hadron Collider]\x01
$BuildingUnlocked[Fusion Power Plant]\x01
 BuildingUnlocked[Space Elevator]\x01
 BuildingUnlocked[Medical Center]\x01
#BuildingUnlocked[Statue of Liberty]\x01
!BuildingUnlocked[Arc de Triomphe]\x01
\x1eBuildingUnlocked[Eiffel Tower]\x01
(BuildingUnlocked[Grand Central Terminal]\x01
\x1dBuildingUnlocked[LuxuryHotel]\x01
\x18BuildingUnlocked[Casino]\x01
\x15BuildingUnlocked[Zoo]\x01
\x1eBuildingUnlocked[DrivingRange]\x01
 BuildingUnlocked[Fancy Fountain]\x01
 BuildingUnlocked[Meteorite Park]\x01
 
BuildingUnlocked[Doomsday Vault]\x01
#BuildingUnlocked[Disaster Memorial]\x01
.BuildingUnlocked[Sparkly Unicorn Rainbow Park]\x01
#BuildingUnlocked[Pyramid Of Safety]\x01
%BuildingUnlocked[Sphinx Of Scenarios]\x01
\x1dBuildingUnlocked[Steam Train]\x01
*BuildingUnlocked[Ultimate Recycling Plant]\x01
*BuildingUnlocked[Climate Research Station]\x01
"BuildingUnlocked[Floating Gardens]\x01
$BuildingUnlocked[Bird and Bee Haven]\x01
\x1dBuildingUnlocked[Clock Tower]\x01
#BuildingUnlocked[Old Market Street]\x01
*BuildingUnlocked[Castle Of Lord Chirpwick]\x01
5BuildingUnlocked[Large Pedestrian Area Service Point]\x01
-BuildingUnlocked[Landmark Commercial High 01]\x01
.BuildingUnlocked[Landmark Residential High 01]\x01
)BuildingUnlocked[Landmark Office High 01]\x01
5BuildingUnlocked[Small Pedestrian Area Service Point]\x01
+BuildingUnlocked[Large Cargo Service Point]\x01
-BuildingUnlocked[Large Garbage Service Point]\x01
+BuildingUnlocked[Small Cargo Service Point]\x01
-BuildingUnlocked[Small Garbage Service Point]\x01
&BuildingUnlocked[Large Fountain Plaza]\x01
7BuildingUnlocked[Landmark Museum of Post-Modern Art 01]\x01
)BuildingUnlocked[Landmark Market Hall 01]\x01
+BuildingUnlocked[Landmark Shopping Mall 01]\x01
!BuildingUnlocked[Flower Plaza 01]\x01
;BuildingUnlocked[Large Pedestrian Area Plaza - Summer Only]\x01
\x19BuildingUnlocked[Bank 02]\x01
$BuildingUnlocked[Financial Plaza 01]\x01
$BuildingUnlocked[Financial Plaza 02]\x01
\x1cBuildingUnlocked[Bronze Cow]\x01
\x1eBuildingUnlocked[Bronze Panda]\x01
.BuildingUnlocked[International Trade Building]\x01
\x19BuildingUnlocked[Bank 03]\x01
\x19BuildingUnlocked[Bank 01]\x01
#BuildingUnlocked[Festival Fan Zone]\x01
"BuildingUnlocked[Live Music Venue]\x01
92862940316 Extra Landscaping Tools [1.15929673530.enabled\x01
\x0fPloppableButton\x00
\x06Police\x00
\x11InfoViewFinancial\x00
\x0eFireDepartment\x00
\nHealthcare\x00
\x0fPublicTransport\x00
\x08Policies\x00
\rInfoViewLevel\x00
\x05Roads\x00
\tEducation\x00
\x06Zoning\x00
\tMonuments\x00
\x11InfoViewLandValue\x00
\x0bElectricity\x00
\x0bLandscaping\x00
\x08District\x00
\x07Wonders\x00
\x11InfoViewEducation\x00
\x05Water\x00
\x08Resource\x00
\x11InfoViewResources\x00
\x07Garbage\x00
\x08Industry\x00
3672248733 Ultimate Eyecandy v1.5-1485519882.enabled\x01
.2126383845 Real Time Offline1157273189.enabled\x01
\x14ForestBrushRevisited\x00
\x0eBeautification\x00
\x0ePedestrianArea\x00
\x0eWaterAndSewage\x00
\x15InfoViewTrafficRoutes\x00
\rInfoViewTours\x00
\x17InfoViewPublicTransport\x00
\x15InfoViewTerrainHeight\x00
\x0fInfoViewTourism\x00
\x13InfoViewDestruction\x00
\x19InfoViewDisasterDetection\x00
\x0eInfoViewHealth\x00
\x11InfoViewDistricts\x00
\x15InfoViewEntertainment\x00
42804719780 Transfer Manager CE v2.1542056446.enabled\x01
92864913941 Surface Painter temporary fix718499042.enabled\x01
22594569657 Parking Lot Snapping-1808315216.enabled\x01
.2891132324 Road Builder v1.01606605905.enabled\x01
\x07Surface\x00
\x19InfoViewTrafficCongestion\x00
\nCampusArea\x00
\x11InfoViewHappiness\x00
\x12InfoViewPopulation\x00
\x0bAirportArea\x00
.2527486462 Tree Anarchy 1.3-1033147225.enabled\x01
\x00
\x00
\x00
\x00
\x02\x00
\x00
\x00
\x0cpdx_acc_lsid\x1176561197960267366\x0bpdx_acc_sid\x00
\x00
\x00
\x00
\x00
'''

s = re.sub(r'\\x([0-9a-fA-F]+)', "$${}$$".format(lambda m: str(int(m.group(0), 16))), a.decode())
print(s)