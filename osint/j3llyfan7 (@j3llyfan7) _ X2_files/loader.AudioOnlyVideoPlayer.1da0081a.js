var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

"use strict";(self.webpackChunk_twitter_responsive_web=self.webpackChunk_twitter_responsive_web||[]).push([["loader.AudioOnlyVideoPlayer"],{50744:(e,t,n)=>{n.r(t),n.d(t,{__DANGEROUS_IMPORT_VIDEOPLAYER_BASE__:()=>P,__DANGEROUS_IMPORT__:()=>A});n(6886);var o=n(2784),i=n(25686),a=n(6556),r=n(38250),s=n(73186),l=n(45843),c=n(69058),u=n(99959),p=n(92462),y=n(48501),d=n(92160);const f=()=>(e,t,{api:n})=>n.getHttpClient(),_=(0,d.Z)().propsFromActions((()=>({getTwitterAuthedHttpClient:f}))).withAnalytics();var m=n(7187),b=n(75845);function g(e){const{featureSwitches:t}=o.useContext(y.rC),{acquisitionParams:n,broadcastId:i,isLive:r,isLooping:s,media:l,mediaKey:d,onEnded:f,onPlaybackEmitterCreated:_,onPlayerApi:g,onPlayerState:P,requestedTimecode:A,shouldAutoplayMuted:E}=e,[T,w]=o.useState(null),h=o.useRef({playbackCoordinationEmitter:null,previousPlayerState:null}),S=l||i&&d;if(o.useEffect((()=>{null===T&&S&&(0,u.ij)({showControls:!1,source:{}},t).then((e=>w((()=>e))))}),[T,S,t]),o.useEffect((()=>function(){const{playbackCoordinationEmitter:e}=h.current;e&&e.unregister()}),[]),null===T||!S)return null;const R=Boolean(r&&i&&d),I=!R&&E,M=R?a.W.SPACE:a.W.NORMAL;const O=function(e,t){const n=e.analytics.contextualScribeNamespace,o={isAnonymous:t.isTrue("spaces_incognito_consumption_enabled")&&e.isAnonymous,enableShortFormCompleteLogging:t.isTrue("responsive_web_video_pcomplete_enabled"),periscopeAuthToken:b.w.proxsee.authToken(),scribeContext:{...n},userType:b.w.proxsee.userType()},i={log:t=>{const{category:n,data:o,namespace:i}=t;null!=i&&i.action&&e.analytics.scribe({...i,data:{...o,_category_:n}})}};return new m.Z(i,{log:()=>{}},e.getTwitterAuthedHttpClient(),o)}(e,t),Z={analytics:O,basePlayerClass:T,httpClient:v,onApiReady:function(t){var n;I||t.play(),"function"==typeof g&&g(t);const o=null==l||null==(n=l.video_info)?void 0:n.duration_millis;"number"==typeof o&&"number"==typeof A&&t.scrubToFraction(A/o);const i={onAutoPlayRequest:function(){I&&t.playPreview()},onPauseRequest:function(){e.disablePlaybackCoordination||t.pause()},playbackPriority:M,canAutoplay:Boolean(E),isLooping:Boolean(s)};h.current.playbackCoordinationEmitter=p.Tc.register(i),_&&_(h.current.playbackCoordinationEmitter)},onStateUpdate:function(e,t){"function"==typeof P&&P(e,t),function(e){const t=k(e);e.isPlaying&&t&&t.durationMs===t.currentTimeMs&&"function"==typeof f&&(f(),h.current.playbackCoordinationEmitter&&h.current.playbackCoordinationEmitter.signalPlaybackFinish())}(e),function(e){const{playbackCoordinationEmitter:t,previousPlayerState:n}=h.current,o=null===n,i=null==n?void 0:n.isPlaying,a=e.isPlaying,r=!o&&i&&!a;!o&&i||!a?r&&t&&t.signalPause():t&&t.signalPlay()}(e),h.current.previousPlayerState=e},twitterAuthedHttpClient:e.getTwitterAuthedHttpClient()};if(i&&d){const e={...Z,configType:"static",contentId:d,contentType:"broadcast",variants:[],videoId:c.Z.forAudioSpace(i,d,r,n)};return o.createElement(C,{key:i,playerConfig:e})}if(l){const e={...Z,configType:"static",contentId:l.id_str,loop:!1,contentType:"media_entity",durationMs:l.video_info.duration_millis,variants:l.video_info.variants.map((({bitrate:e,content_type:t,url:n})=>({type:t,src:n})))};return o.createElement(C,{key:l.id_str,playerConfig:e})}return null}function C({playerConfig:e}){return o.createElement(i.Z,{style:E.displayNone},o.createElement(r.Z,e))}const P=g,A=o.memo(_(g)),k=e=>e&&e.tracks[e.currentTrackId],v=new l.ZP({}),E=s.default.create((e=>({displayNone:{display:"none"}})))},55249:(e,t,n)=>{n.d(t,{Z:()=>o});const o=(e,t)=>{let n=null;const o=()=>{n=null,e()};return()=>(n||(n=t(o)),n)}}}]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/loader.AudioOnlyVideoPlayer.1da0081a.js.map

}
/*
     FILE ARCHIVED ON 16:55:46 Mar 25, 2024 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 01:49:24 Jun 20, 2024.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.571
  exclusion.robots: 0.068
  exclusion.robots.policy: 0.058
  esindex: 0.009
  cdx.remote: 8.455
  LoadShardBlock: 281.043 (17)
  PetaboxLoader3.datanode: 216.049 (18)
  load_resource: 109.719
  PetaboxLoader3.resolve: 95.087
*/