<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.12.2" name="terrain_atlas" tilewidth="32" tileheight="32" tilecount="1024" columns="32">
 <image source="../Tilesets/Atlas/terrain_atlas.png" width="1024" height="1024"/>
 <tile id="405">
  <animation>
   <frame tileid="405" duration="500"/>
   <frame tileid="437" duration="500"/>
   <frame tileid="469" duration="500"/>
  </animation>
 </tile>
 <tile id="406">
  <animation>
   <frame tileid="406" duration="500"/>
   <frame tileid="438" duration="500"/>
   <frame tileid="470" duration="500"/>
  </animation>
 </tile>
 <tile id="407">
  <animation>
   <frame tileid="407" duration="500"/>
   <frame tileid="439" duration="500"/>
   <frame tileid="471" duration="500"/>
  </animation>
 </tile>
 <tile id="437">
  <animation>
   <frame tileid="437" duration="500"/>
   <frame tileid="469" duration="500"/>
   <frame tileid="405" duration="500"/>
  </animation>
 </tile>
 <tile id="438">
  <animation>
   <frame tileid="438" duration="500"/>
   <frame tileid="470" duration="500"/>
   <frame tileid="406" duration="500"/>
  </animation>
 </tile>
 <tile id="439">
  <animation>
   <frame tileid="439" duration="500"/>
   <frame tileid="471" duration="500"/>
   <frame tileid="407" duration="500"/>
  </animation>
 </tile>
 <tile id="501">
  <animation>
   <frame tileid="501" duration="500"/>
   <frame tileid="469" duration="500"/>
  </animation>
 </tile>
 <tile id="502">
  <animation>
   <frame tileid="502" duration="500"/>
   <frame tileid="470" duration="500"/>
  </animation>
 </tile>
 <tile id="503">
  <animation>
   <frame tileid="503" duration="500"/>
   <frame tileid="471" duration="500"/>
  </animation>
 </tile>
 <wangsets>
  <wangset name="Sand" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="16" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="17" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="48" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="49" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="79" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="80" wangid="0,0,0,1,1,1,0,0"/>
   <wangtile tileid="81" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="111" wangid="0,1,1,1,0,0,0,0"/>
   <wangtile tileid="112" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="113" wangid="0,0,0,0,0,1,1,1"/>
   <wangtile tileid="143" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="144" wangid="1,1,0,0,0,0,0,1"/>
   <wangtile tileid="145" wangid="0,0,0,0,0,0,0,1"/>
   <properties>
    <property name="Sand" value=""/>
   </properties>
  </wangset>
  <wangset name="Grass" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="22" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="23" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="54" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="55" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="85" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="86" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="87" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="117" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="118" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="119" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="149" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="150" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="151" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
  <wangset name="Dark grass" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="775" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="776" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="807" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="808" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="838" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="839" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="840" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="870" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="871" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="872" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="902" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="903" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="904" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
  <wangset name="Dark desert" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="836" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="837" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="868" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="869" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="899" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="900" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="901" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="931" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="932" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="933" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="963" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="964" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="965" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
  <wangset name="City" type="mixed" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="848" wangid="0,1,1,1,1,1,0,1"/>
   <wangtile tileid="849" wangid="0,1,1,1,1,1,1,1"/>
   <wangtile tileid="850" wangid="0,1,0,1,1,1,1,1"/>
   <wangtile tileid="880" wangid="1,1,1,1,1,1,0,1"/>
   <wangtile tileid="881" wangid="1,1,1,1,1,1,1,1"/>
   <wangtile tileid="882" wangid="1,1,0,1,1,1,1,1"/>
   <wangtile tileid="912" wangid="1,1,1,1,0,1,0,1"/>
   <wangtile tileid="913" wangid="1,1,1,1,0,1,1,1"/>
   <wangtile tileid="914" wangid="1,1,0,1,0,1,1,1"/>
  </wangset>
  <wangset name="River" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="298" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="299" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="330" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="331" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="361" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="362" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="363" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="393" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="394" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="395" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="425" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="426" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="427" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
  <wangset name="Cliff" type="mixed" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="69" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="70" wangid="0,0,0,1,1,1,0,0"/>
   <wangtile tileid="71" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="101" wangid="1,1,1,1,1,0,0,0"/>
   <wangtile tileid="102" wangid="1,1,0,1,1,1,1,1"/>
   <wangtile tileid="103" wangid="1,0,0,0,1,1,1,1"/>
   <wangtile tileid="133" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="134" wangid="1,1,0,0,0,0,0,1"/>
   <wangtile tileid="135" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
  <wangset name="Path" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="19" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="20" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="51" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="52" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="82" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="83" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="84" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="114" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="116" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="146" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="147" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="148" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
 </wangsets>
</tileset>
