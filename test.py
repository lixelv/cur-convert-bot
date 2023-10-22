import requests
from bs4 import BeautifulSoup

result = {}

html = """<html><head>
<meta charset="utf-8">
 
 
  
<title>Страны/территории и коды валют</title>
<link rel="StyleSheet" href="../MasterStyleSheet.css" type="text/css">










 
 
 









<meta name="TagDate" content="11/30/2020 12:00:00 AM">
<meta name="Drop" content="WS2021_Translated_WeekendCommercialDelivery1908_ER_Production">
<meta name="WSVersion" content="A">
<meta name="DCSext.WLDSHIP_ver" content="WSA">
<meta name="DCSext.pCC" content="RU">
<meta name="DCSext.pLL" content="RU">
<meta name="DCSext.pPID" content="CORE/Codes/Country_Territory_and_Currency_Codes.htm">
<meta name="DCS.dcsuri" content="worldshiphelp/WSA/RUS/AppHelp/mergedProjects/CORE/Codes/Country_Territory_and_Currency_Codes.htm">
<meta name="DCSext.pSA" content="Resources">
<meta name="DCSext.pSU" content="WorldShip">
<meta name="search" content="<SearchParameters><SupportCategory><Category>Worldship</Category></SupportCategory><AccountSegment>None</AccountSegment><Privilege>None</Privilege></SearchParameters>">
<iframe src="javascript:void(0)" title="" role="presentation" style="width: 0px; height: 0px; border: 0px; display: none;"></iframe><script type="text/javascript" async="" charset="utf-8" id="utag_657" src="//bat.bing.com/bat.js"></script><script type="text/javascript" async="" src="//aap-p.ups.com/script.js"></script><script src="//tags.tiqcdn.com/utag/ups/maestro/prod/utag.js" type="text/javascript" async=""></script><script type="text/javascript" src="https://www.ups.com/assets/090fe25490ceb2cb6785ea730fd896f2d0453d5260d"></script><script>
// akam-sw.js install script version 1.3.6
"serviceWorker"in navigator&&"find"in[]&&function(){var e=new Promise(function(e){"complete"===document.readyState||!1?e():(window.addEventListener("load",function(){e()}),setTimeout(function(){"complete"!==document.readyState&&e()},1e4))}),n=window.akamServiceWorkerInvoked,r="1.3.6";if(n)aka3pmLog("akam-setup already invoked");else{window.akamServiceWorkerInvoked=!0,window.aka3pmLog=function(){window.akamServiceWorkerDebug&&console.log.apply(console,arguments)};function o(e){(window.BOOMR_mq=window.BOOMR_mq||[]).push(["addVar",{"sm.sw.s":e,"sm.sw.v":r}])}var i="/akam-sw.js",a=new Map;navigator.serviceWorker.addEventListener("message",function(e){var n,r,o=e.data;if(o.isAka3pm)if(o.command){var i=(n=o.command,(r=a.get(n))&&r.length>0?r.shift():null);i&&i(e.data.response)}else if(o.commandToClient)switch(o.commandToClient){case"enableDebug":window.akamServiceWorkerDebug||(window.akamServiceWorkerDebug=!0,aka3pmLog("Setup script debug enabled via service worker message"),v());break;case"boomerangMQ":o.payload&&(window.BOOMR_mq=window.BOOMR_mq||[]).push(o.payload)}aka3pmLog("akam-sw message: "+JSON.stringify(e.data))});var t=function(e){return new Promise(function(n){var r,o;r=e.command,o=n,a.has(r)||a.set(r,[]),a.get(r).push(o),navigator.serviceWorker.controller&&(e.isAka3pm=!0,navigator.serviceWorker.controller.postMessage(e))})},c=function(e){return t({command:"navTiming",navTiming:e})},s=null,m={},d=function(){var e=i;return s&&(e+="?othersw="+encodeURIComponent(s)),function(e,n){return new Promise(function(r,i){aka3pmLog("Registering service worker with URL: "+e),navigator.serviceWorker.register(e,n).then(function(e){aka3pmLog("ServiceWorker registration successful with scope: ",e.scope),r(e),o(1)}).catch(function(e){aka3pmLog("ServiceWorker registration failed: ",e),o(0),i(e)})})}(e,m)},g=navigator.serviceWorker.__proto__.register;if(navigator.serviceWorker.__proto__.register=function(n,r){return n.includes(i)?g.call(this,n,r):(aka3pmLog("Overriding registration of service worker for: "+n),s=new URL(n,window.location.href),m=r,navigator.serviceWorker.controller?new Promise(function(n,r){var o=navigator.serviceWorker.controller.scriptURL;if(o.includes(i)){var a=encodeURIComponent(s);o.includes(a)?(aka3pmLog("Cancelling registration as we already integrate other SW: "+s),navigator.serviceWorker.getRegistration().then(function(e){n(e)})):e.then(function(){aka3pmLog("Unregistering existing 3pm service worker"),navigator.serviceWorker.getRegistration().then(function(e){e.unregister().then(function(){return d()}).then(function(e){n(e)}).catch(function(e){r(e)})})})}else aka3pmLog("Cancelling registration as we already have akam-sw.js installed"),navigator.serviceWorker.getRegistration().then(function(e){n(e)})}):g.call(this,n,r))},navigator.serviceWorker.controller){var u=navigator.serviceWorker.controller.scriptURL;u.includes("/akam-sw.js")||u.includes("/akam-sw-preprod.js")||u.includes("/threepm-sw.js")||(aka3pmLog("Detected existing service worker. Removing and re-adding inside akam-sw.js"),s=new URL(u,window.location.href),e.then(function(){navigator.serviceWorker.getRegistration().then(function(e){m={scope:e.scope},e.unregister(),d()})}))}else e.then(function(){window.akamServiceWorkerPreprod&&(i="/akam-sw-preprod.js"),d()});if(window.performance){var w=window.performance.timing,l=w.responseEnd-w.responseStart;c(l)}e.then(function(){t({command:"pageLoad"})});var k=!1;function v(){window.akamServiceWorkerDebug&&!k&&(k=!0,aka3pmLog("Initializing debug functions at window scope"),window.aka3pmInjectSwPolicy=function(e){return t({command:"updatePolicy",policy:e})},window.aka3pmDisableInjectedPolicy=function(){return t({command:"disableInjectedPolicy"})},window.aka3pmDeleteInjectedPolicy=function(){return t({command:"deleteInjectedPolicy"})},window.aka3pmGetStateAsync=function(){return t({command:"getState"})},window.aka3pmDumpState=function(){aka3pmGetStateAsync().then(function(e){aka3pmLog(JSON.stringify(e,null,"\t"))})},window.aka3pmInjectTiming=function(e){return c(e)},window.aka3pmUpdatePolicyFromNetwork=function(){return t({command:"pullPolicyFromNetwork"})})}v()}}();</script>
<script type="text/javascript" language="javascript1.2" src="https://www.ups.com/assets/tealium/tealium_wt.js"></script>

<script>(window.BOOMR_mq=window.BOOMR_mq||[]).push(["addVar",{"rua.upush":"false","rua.cpush":"false","rua.upre":"false","rua.cpre":"false","rua.uprl":"false","rua.cprl":"false","rua.cprf":"false","rua.trans":"","rua.cook":"false","rua.ims":"false","rua.ufprl":"false","rua.cfprl":"false","rua.isuxp":"false","rua.texp":"norulematch"}]);</script>
                              <script>!function(a){var e="https://s.go-mpulse.net/boomerang/",t="addEventListener";if("False"=="True")a.BOOMR_config=a.BOOMR_config||{},a.BOOMR_config.PageParams=a.BOOMR_config.PageParams||{},a.BOOMR_config.PageParams.pci=!0,e="https://s2.go-mpulse.net/boomerang/";if(window.BOOMR_API_key="TADEN-6MDCS-UHH5M-YHPKQ-2GBH3",function(){function n(e){a.BOOMR_onload=e&&e.timeStamp||(new Date).getTime()}if(!a.BOOMR||!a.BOOMR.version&&!a.BOOMR.snippetExecuted){a.BOOMR=a.BOOMR||{},a.BOOMR.snippetExecuted=!0;var i,_,o,r=document.createElement("iframe");if(a[t])a[t]("load",n,!1);else if(a.attachEvent)a.attachEvent("onload",n);r.src="javascript:void(0)",r.title="",r.role="presentation",(r.frameElement||r).style.cssText="width:0;height:0;border:0;display:none;",o=document.getElementsByTagName("script")[0],o.parentNode.insertBefore(r,o);try{_=r.contentWindow.document}catch(O){i=document.domain,r.src="javascript:var d=document.open();d.domain='"+i+"';void(0);",_=r.contentWindow.document}_.open()._l=function(){var a=this.createElement("script");if(i)this.domain=i;a.id="boomr-if-as",a.src=e+"TADEN-6MDCS-UHH5M-YHPKQ-2GBH3",BOOMR_lstart=(new Date).getTime(),this.body.appendChild(a)},_.write("<bo"+'dy onload="document._l();">'),_.close()}}(),"".length>0)if(a&&"performance"in a&&a.performance&&"function"==typeof a.performance.setResourceTimingBufferSize)a.performance.setResourceTimingBufferSize();!function(){if(BOOMR=a.BOOMR||{},BOOMR.plugins=BOOMR.plugins||{},!BOOMR.plugins.AK){var e=""=="true"?1:0,t="",n="jyswyuaxeluxyzjvrvta-f-6185ce0f4-clientnsv4-s.akamaihd.net",i="false"=="true"?2:1,_={"ak.v":"36","ak.cp":"14334","ak.ai":parseInt("265833",10),"ak.ol":"0","ak.cr":28,"ak.ipv":4,"ak.proto":"h2","ak.rid":"114e9a5a","ak.r":23191,"ak.a2":e,"ak.m":"dsca","ak.n":"essl","ak.bpcip":"78.37.108.0","ak.cport":64534,"ak.gh":"2.21.96.29","ak.quicv":"","ak.tlsv":"tls1.3","ak.0rtt":"","ak.csrc":"-","ak.acc":"","ak.t":"1698008422","ak.ak":"hOBiQwZUYzCg5VSAfCLimQ==vNNIRLzuWe5oBUXkvCVLTuA6imoTu8OOFZ0oiQmOLZf7nk4Skp+mS9CP+UPZTX1BA0DMUaj/NJqn5q8z2iPhre6eZABka84hqrwPcMOwVpQ2Ia9FvfLGerKOlEddFTh9jfaUUH6yT3qm+9MFOTQhnRjr0oAeHTFyg39VJ5yY7paCwN9da+eH7J/wQ//6uHNYCEhVw0TFj1HYZ5tL60uV3AHso9Re4EOtwj/g5c88XHw0Tfa2yYbEhwp/YOpEW0v4jlKMAXt/NDVqpxR2zbxLqwsnffmMLa5H7/AYIpdCPPLxhQNX7hs03xuc14qSsDg08kc8N1ZkP6yxVd3whSletA7vcVmDpS80HXyatMDQVnn0OE823UgSUdfou0AivxrPGHT7P6Pxs0v89NPOKhchAeRXQX0nfSmlO/MlTjVt048=","ak.pv":"193","ak.dpoabenc":"","ak.tf":i};if(""!==t)_["ak.ruds"]=t;var o={i:!1,av:function(e){var t="http.initiator";if(e&&(!e[t]||"spa_hard"===e[t]))_["ak.feo"]=void 0!==a.aFeoApplied?1:0,BOOMR.addVar(_)},rv:function(){var a=["ak.bpcip","ak.cport","ak.cr","ak.csrc","ak.gh","ak.ipv","ak.m","ak.n","ak.ol","ak.proto","ak.quicv","ak.tlsv","ak.0rtt","ak.r","ak.acc","ak.t","ak.tf"];BOOMR.removeVar(a)}};BOOMR.plugins.AK={akVars:_,akDNSPreFetchDomain:n,init:function(){if(!o.i){var a=BOOMR.subscribe;a("before_beacon",o.av,null,null),a("onbeacon",o.rv,null,null),o.i=!0}return this},is_complete:function(){return!0}}}}()}(window);</script><style type="text/css"> #__tealiumImplicitmodal {  display: none;}        @media (min-width: 768px) {            .implicit_privacy_prompt.implicit_consent {                position: fixed;                width: 75%;                left: 50%;                text-align: left;                background-color: #F7F6F5;                font-size: 1.3rem;                z-index: 99998;                font-family: Tahoma,helvetica,arial,sans-serif;                color: #242424;                border: 1px solid #757575;                transform: translate(-50%, 0);                bottom: 0;                max-width: 1400px;                box-shadow: 0 0px 15px #0005;            }        }            @media (min-width: 320px) and (max-width: 767px) {            .implicit_privacy_prompt.implicit_consent {                position: fixed;                width: 100%;                left: 0%;                text-align: left;                background-color: #F7F6F5;                font-size: 1.3rem;                z-index: 99998;                font-family: Tahoma,helvetica,arial,sans-serif;                color: #242424;                border: 1px solid #757575;                transform: none;                bottom: 0;                max-width: 1400px;                box-shadow: 0 0px 15px #0005;            }        }    .ups-readerTxt {position: absolute !important;clip: rect(1px, 1px, 1px, 1px);padding: 0 !important;border: 0 !important;height: 1px !important;width: 1px !important;overflow: hidden;}.__tealiumPrivacyBackdrop{display: block !important;}.implicit_privacy_prompt.implicit_consent .implicit_privacy_prompt_content {  width: 100%;  max-width: 85%;  margin: 0 auto;  padding: 10px;  font-size: 14px;  position: relative;}        @media (min-width: 320px) and (max-width: 767px) {            .implicit_privacy_prompt.implicit_consent .implicit_privacy_prompt_content {                max-width: 100%;                padding: 15px;            }        }    .implicit_privacy_prompt.implicit_consent .implicit_consent_title {  font-size: 1.1em;  font-weight: bold;  line-height: 1.25;  margin: 0;}.implicit_privacy_prompt.implicit_consent .implicit_consent__inner {  display: table;  width: 100%;}.implicit_privacy_prompt.implicit_consent .implicit_consent__inner-left,.implicit_privacy_prompt.implicit_consent .implicit_consent__inner-right {  display: table-cell;  vertical-align: left;}.implicit_privacy_prompt.implicit_consent .implicit_consent__inner-left p {  margin: 0 0 10px;  font-size: 14px;  line-height: 1.25;}.implicit_privacy_prompt.implicit_consent .implicit_consent__inner-left a,.implicit_privacy_prompt.implicit_consent .implicit_consent__inner-right a {  text-decoration: underline;  color: #426DA9;}.implicit_privacy_prompt.implicit_consent .implicit_consent__inner-right {  width: 100px;  padding-left: .5rem;  text-align: center;  vertical-align: middle;}.implicit_privacy_prompt #implicit_consent_prompt_submit:hover {  transition: background-color 0.2s ease;  background-color: #016862;}#__tealiumImplicitmodal .implicit_privacy_prompt>.close_btn_thick {  position: absolute;  display: block;  top: 13px;  right: 10px;  text-decoration: none;  text-shadow: none;  color: #4A4A4A; font: 14px/100% arial, sans-serif; font-weight: normal; cursor: pointer;  background: none;  padding-left: 5px;  padding-right: 5px;  border: 0px solid #000000;  z-index: 99;}</style><script type="text/javascript" async="" charset="utf-8" id="utag_ups.maestro_364" src="//tags.tiqcdn.com/utag/ups/maestro/prod/utag.364.js?utv=ut4.48.202310121127"></script><script type="text/javascript" async="" charset="utf-8" id="utag_ups.maestro_616" src="//tags.tiqcdn.com/utag/ups/maestro/prod/utag.616.js?utv=ut4.48.202310051201"></script><script type="text/javascript" async="" charset="utf-8" id="utag_ups.maestro_657" src="//tags.tiqcdn.com/utag/ups/maestro/prod/utag.657.js?utv=ut4.48.202308170328"></script><script src="https://ups.blueconic.net/DG/DEFAULT/cs?&amp;callback=bc_json527" async=""></script><script type="text/javascript" async="" charset="utf-8" id="tealium_visitor_service_616maestro_1" src="https://visitor-service.tealiumiq.com/ups/maestro/018b5930d1e3001b3a62173842360406f007406701298?callback=utag.ut%5B%22writevamaestro%22%5D&amp;rnd=1698008477545"></script><script src="https://ups.blueconic.net/DG/DEFAULT/cs?bcsessionid=57012912-6dde-49be-bba8-bb074b6eda8b&amp;&amp;callback=bc_json528" async=""></script></head><iframe style="width: 0px; height: 0px; display: none;"></iframe>
<body>


<h1>Страны/территории и коды валют</h1>
<table cellspacing="0" width="100.214%">
<colgroup><col style="width: 25.094%;">
<col style="width: 12.923%;">
<col style="width: 12.793%;">
<col style="width: 12.961%;">
<col style="width: 36.229%;">
</colgroup><tbody><tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">&nbsp;
<p style="font-size: 10pt; font-weight: bold; margin-top: 6pt;"><span style="margin-top: 6.00pt;">Страна/территория</span></p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="font-size: 10pt; font-weight: bold; margin-top: 6pt;">Код<br>
UPS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="font-size: 10pt; font-weight: bold; margin-top: 6pt;">Код<br>
IATA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="font-size: 10pt; font-weight: bold; margin-top: 6pt;">Код валюты</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">&nbsp;
<p style="font-size: 10pt; font-weight: bold; margin-top: 6pt;">Название валюты</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Австралия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AUD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Австралийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Австрия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Азербайджан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AZM</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Азербайджанский манат</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Азорские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">A2</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Аландские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AX</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AX</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Албания</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Алжир</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DZD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Алжирский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Американское Самоа</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ангилья</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Англия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ангола</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AOA</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ангольская кванза</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Андорра</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AD</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AD</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Антигуа и Барбуда</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Аргентина</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ARS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Аргентинский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Армения</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AMD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Армянский драм</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Аруба</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AWG</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Арубский гульден/флорин</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Афганистан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Афгани</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Багамские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BSD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Багамский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бангладеш</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BD</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BD</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BDT</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бангладешская така</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Барбадос</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BB</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BBD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Барбадосский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бахрейн</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BHD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бахрейнский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Белиз</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BZD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Белизский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Белоруссия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BYR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Белорусский рубль</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бельгия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бенин</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BJ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BJ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бермудские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BMD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бермудский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Болгария</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Боливия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BOB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Боливийский боливиано</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Босния</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BAM</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Боснийская марка</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ботсвана</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BWP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ботсванская пула</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бразилия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BRL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бразильский реал</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британские Виргинские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бруней</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BND</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Брунейский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Буркина-Фасо</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бурунди</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BIF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бурундийский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бутан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BTN</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Бутанский нгултрум</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Вануату</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VUV</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Вануатский вату</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Венгрия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HUF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Венгерский форинт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Венесуэла</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VEB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Венесуэльский боливар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Вирджин-Горда</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточный Тимор</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Вьетнам</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VND</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Вьетнамский донг</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Габон</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XAF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гайана</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GYD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гайанский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гаити</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HTG</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гаитянский гурд</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гамбия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GMD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гамбийский даласи</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гана</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GHS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ганский седи</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гваделупа</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GP</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гватемала</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GTQ</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гватемальский кетсаль</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гвинея</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GNF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гвинейский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гвинея-Бисау</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Германия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гернси</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гибралтар</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GIP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гибралтарский фунт стерлингов</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Голландия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гондурас</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HNL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гондурасская лемпира</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гонконг</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HKD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гонконгский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Город-государство Ватикан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гренада</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GD</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GD</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гренландия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DKK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Датская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Греция</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Грузия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GEL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Грузинский лари</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Гуам</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Дания</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DKK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Датская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Демократическая Республика Конго</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CD</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CD</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CDF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Конголезский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Джерси</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Джибути</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DJ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DJ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DJF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Джибутийский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доминика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доминиканская Республика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DOP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доминиканский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Европа</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EP</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Египет</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EGP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Египетский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Замбия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZMK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Замбийская квача</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Зимбабве</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZWD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Зимбабвийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Йемен</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">YE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">YE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">YER</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Йеменский риал</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Израиль</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ILS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Израильский шекель</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Индия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">INR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Индийская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Индонезия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ID</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ID</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IDR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Индонезийская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Иордания</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JOD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Иорданский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ирак</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IQ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IQ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NID</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Иракский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ирландская Республика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Исландия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ISK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Исландская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Испания</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ES</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ES</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Италия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Казахстан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KZT</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Казахский тенге</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Каймановы острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KYD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кайманский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Камбоджа</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KHR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Камбоджийский риель</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Камерун</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XAF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;"><a name="Canada" id="Canada"></a>Канада</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CAD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Канадский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Канарские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">IC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ES</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Катар</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">QA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">QA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">QAR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Катарский риал</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кения</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KES</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кенийский шиллинг</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кипр</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Киргизстан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KGS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Киргизский сом</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кирибати</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AUD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Австралийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Китайская Народная Республика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RMB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Китайский юань</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Колумбия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">COP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Колумбийский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Коморские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Коморский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Конго</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XAF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Косово</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KV</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Косраэ</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Коста-Рика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CRC</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Коста-риканский колон</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кот-д'Ивуар</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;"><a name="Cuba_IATA_Code" id="Cuba_IATA_Code"></a>Куба</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CU</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кубинский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кувейт</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KWD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кувейтский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Кюрасао</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Лаос</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LAK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Лаосский кип</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;"><a name="Latvia_EUR"></a>Латвия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LV</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Лесото</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LSL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Лесотский лоти</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Либерия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LRD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Либерийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ливан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LB</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ливанский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ливия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LYD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ливийский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Литва</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Лихтенштейн</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CHF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Швейцарский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Люксембург</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Маврикий</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Маврикийская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мавритания</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MRO</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мавританская угия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мадагаскар</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MGA</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Малагасийский ариари</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мадейра</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">M3</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Майотте</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">YT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">YT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Макау</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MOP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Патака Макао</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Македония (бывшая Югославская Республика Македония)</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Малави</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MWK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Малавийская квача</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Малайзия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MYR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Малайзийский ринггит</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мали</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ML</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ML</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мальдивские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MV</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MVR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мальдивская руфия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мальта</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Марокко</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MAD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Марокканский дирхам</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мартиника</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MQ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MQ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Маршалловы острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мексика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MX</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MX</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MXN</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мексиканский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мелилья</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мозамбик</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MZM</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Мозамбикский метикаль</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Молдова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MD</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MD</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MDL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Молдавский лей</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Монако</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Монголия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MNT</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Монгольский тугрик</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Монтсеррат</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Намибия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NAD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Намибийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Непал</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NP</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NPR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Непальская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Нигер</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Нигерия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NGN</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Нигерийская найра</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Нидерланды</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Никарагуа</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NIO</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Никарагуанская золотая кордоба</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Новая Зеландия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NZD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Новозеландский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Новая Каледония</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XPF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФП</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Норвегия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NOK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Норвежская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">о. Бонайре, о-в Св. Евстатия, Саба</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BQ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BQ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Объединенные Арабские Эмираты</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AED</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Дирхам Объединенных Арабских Эмиратов</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">о-в. Св. Бартоломея</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">о-в. Св. Евстатия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">E2</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BQ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ANG</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Нидерландский Антильский гульден</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">о-в. Св. Крус</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">C3</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">О-ва Уоллис и Футуна</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">WF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">WF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XPF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФП</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Оман</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">OM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">OM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">OMR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Оманский риал</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Остров Норфолк</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AUD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Австралийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Острова Зеленого Мыса</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CV</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CVE</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эскудо Кабо-Верде</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Острова Кука</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NZD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Новозеландский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Острова Юнион</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Пакистан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PKR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Пакистанская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Палау</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Панама</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PAB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Панамский бальбоа</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Папуа-Новая Гвинея</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PGK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Папуасская кина</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Парагвай</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PYG</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Парагвайский гуарани</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Перу</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PEN</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Перуанский нуэво соль</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Польша</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PLN</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Польский злотый</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Понапе</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Португалия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Пуэрто-Рико</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Реюньон</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Россия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RU</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RUB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Российский рубль</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Рота</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Руанда</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RWF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Руандийский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Румыния</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ROL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Румынский лей</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Саба</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">S1</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">BQ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ANG</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Нидерландский Антильский гульден</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сайпан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SP</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Самоа</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">WS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">WS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">WST</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Самоанская тала</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сан-Марино</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сан-Томе и Принципи</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ST</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ST</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">STD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Добра Сан-Томе и Принсипи</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Саудовская Аравия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SAR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Риял Саудовской Аравии</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Свазилендский</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SZL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Свазилендский лилангени</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Северная Ирландия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">NB</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Северные Марианские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MP</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сейшельские Острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SCR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сейшельская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сенегал</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Винсент и Гренадины</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Джон</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Китс и Невис</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Кристофер</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Люсия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XCD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Восточно-карибский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Маартен и о-в Св. Мартина</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SX</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SX</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сент-Томас</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сербия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RS</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">RS</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сербский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сеута</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сингапур</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SGD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сингапурский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Словакия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Словения</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Соединенное Королевство</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GB</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;"><a name="United_States" id="United_States"></a>Соединенные Штаты Америки</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">US</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">US</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Соломоновы Острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SB</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SBD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар Соломоновых островов</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Суринам</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SRG</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Суринамский гульден</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">США Виргинские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сьерра-Леоне</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SLL</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сьерра-Леоне леоне</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Таджикистан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TJ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TJ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TJS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Таджикский сомони</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тайвань</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TW</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TW</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TWD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тайваньский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Таиланд</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">THB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тайский бат</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Таити</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XPF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФП</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Танзания</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TZS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Танзанийский шиллинг</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Теркс и Кайкос</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тиниан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">MP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Того</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XOF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тонга</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TOP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">тонганская паанга</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тортола</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">VG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тринидад и Тобаго</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TT</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TT</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TTD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар Тринидада и Тобаго</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Трук</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TU</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тувалу</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TV</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">AUD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Австралийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тунис</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TN</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TN</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TND</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Тунисский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Туркменистан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TMT</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Туркменский манат</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Турция</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TRY</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Турецкая лира</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Уганда</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UG</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UG</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UGX</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Угандийский шиллинг</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Узбекистан</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UZS</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Узбекский сум</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Украина</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UAH</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Украинская гривна</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Уругвай</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UY</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UY</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">UYU</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Уругвайский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Уэльс</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">WL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Фарерские острова</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FO</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FO</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">DKK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Датская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Федеративные Штаты Микронезии</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Фиджи</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FJ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FJ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FJD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Фиджийский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;"><a name="Philippines_Currency_Code"></a>Филиппины</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PHP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Филиппинский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Финляндия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FI</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FI</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франция</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Французская Гвиана</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Французская Полинезия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">PF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XPF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФП</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Хорватия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">HR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Центральная Африканская Республика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CF</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XAF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Чад</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TD</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">TD</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XAF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Черногория</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ME</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ME</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Сербский динар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Чешская Республика</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CZ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CZ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CZK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Чешская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Чили</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CL</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CL</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CLP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Чилийский песо</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Швейцария</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CH</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CH</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">CHF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Швейцарский франк</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Швеция</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SEK</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Шведская крона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Шотландия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SF</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GB</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GBP</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Британский фунт</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Шри-Ланка</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LK</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LK</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">LKR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Шри-ланкийская рупия</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эквадор</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EC</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EC</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Экваториальная Гвинея</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GQ</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">GQ</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">XAF</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Франк КФА Центрального банка государств Западной Африки</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эль-Сальвадор</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SV</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">SV</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эритрея</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ER</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ER</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ERN</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эритрейская накфа</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эстония</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EE</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EE</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">EUR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">евро</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эфиопия</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ET</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ET</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ETB</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Эфиопский быр</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Южная Африка</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZA</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">ZAR</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Южноафриканский ранд</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Южная Корея</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KR</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KR</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">KRW</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Южнокорейская вона</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ямайка</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JM</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JMD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Ямайский доллар</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Яп</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">YA</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">FM</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">USD</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Доллар США</p>
</td>
</tr>
<tr style="vertical-align: top;">
<td style="width: 25.094%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Япония</p>
</td>
<td style="width: 12.923%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JP</p>
</td>
<td style="width: 12.793%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JP</p>
</td>
<td style="width: 12.961%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">JPY</p>
</td>
<td style="width: 36.229%; padding-left: 1px; padding-top: 1px; padding-right: 1px; padding-bottom: 1px;">
<p style="margin-bottom: 2.00pt;">Японская иена</p>
</td>
</tr>
</tbody></table>

<script type="text/javascript" src="/9zEaE5hve/vI/d_8qYTQ/9a7bz6YtL9/FEF2AQ/dlk3dhZ/VFBAB"></script>

<div id="__tealiumImplicitmodal" style="display: block;"><div class="implicit_privacy_prompt implicit_consent" role="alert">   <button class="close_btn_thick icon ups-icon-x"><span class="ups-readerTxt">Close</span></button>  <div class="implicit_privacy_prompt_content">   <h2 class="implicit_consent_title">На этом сайте используются файлы cookie.</h2>     <div class="implicit_consent__inner">       <div class="implicit_consent__inner-left">        <p>Продолжая работу, вы соглашаетесь на использование файлов cookie. Чтобы узнать дополнительную информацию или установить собственные предпочтения, перейдите по ссылке «Параметры файла cookie» в нижней части любой страницы.</p>      </div>    </div>  </div> </div></div></body><iframe id="KXrMKUBugYzg4HNq" style="display: none;"></iframe><div style="display: none;"></div></html>"""

soup = BeautifulSoup(html, 'html.parser')

sector = soup.find('tbody').find_all('tr')

for el in sector:
    el = el.find_all('td')
    print(len(el))
    result.update({el[3].get_text().replace('\n', ''): el[4].get_text().replace('\n', '')})

print(result)
