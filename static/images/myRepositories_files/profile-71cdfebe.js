System.register(["./chunk-vendor.js","./chunk-frameworks.js"],(function(e,t){"use strict";var n,o,r,s,i;return{setters:[function(e){n=e.o,o=e.a,r=e.r},function(e){s=e.aQ,i=e.a}],execute:function(){n("click",".js-new-user-contrib-example",(async function(e){const t=document.querySelector(".js-calendar-graph");if(t.classList.contains("sample-graph"))return;t.classList.add("sample-graph");const n=e.currentTarget.getAttribute("data-url"),o=await fetch(n,{headers:{"X-Requested-With":"XMLHttpRequest"}});if(!o.ok)return void t.classList.remove("sample-graph");const r=await o.text(),s=document.createElement("div");s.innerHTML=r;t.querySelector(".js-calendar-graph-svg").replaceWith(s.children[0])}));let e=null;function a(){const e=document.querySelector(".js-calendar-graph").getAttribute("data-url");return new URL(e,window.location.origin)}function c(e){const t=e.target;t.matches("rect.day")&&(l(),function(e){const t=e.getAttribute("data-date"),n=function(e,t){const n=`${u[t.getUTCMonth()].slice(0,3)} ${t.getUTCDate()}, ${t.getUTCFullYear()}`,o=0===e?"No":new Intl.NumberFormat("en-US").format(e),r=document.createElement("div");r.classList.add("svg-tip","svg-tip-one-line"),r.style.pointerEvents="none";const s=document.createElement("strong");return s.textContent=`${o} ${1===e?"contribution":"contributions"}`,r.append(s," on "+n),r}(parseInt(e.getAttribute("data-count")||""),j(t));document.body.appendChild(n);const o=e.getBoundingClientRect(),r=o.left+window.pageXOffset-n.offsetWidth/2+o.width/2,s=o.bottom+window.pageYOffset-n.offsetHeight-2*o.height;n.style.top=s+"px",n.style.left=r+"px"}(t))}function l(){const e=document.querySelector(".svg-tip");e&&e.remove()}o(".js-calendar-graph-svg",(function(t){const n=t.closest(".js-calendar-graph");n.addEventListener("mouseover",c),n.addEventListener("mouseout",l);const o=n.getAttribute("data-from");o&&(e=j(o))})),n("click",".js-calendar-graph rect.day",(function(t){const n=t.currentTarget,o=n.closest(".js-calendar-graph").getAttribute("data-org"),r=n.getAttribute("data-date");n.classList.contains("active")?v(S()):function(t,n,o){let r,s;if(e&&n){const n=e.getTime(),o=26784e5,i=n-o,a=n+o;[r,s]=t>e?[e,t]:[t,e],r=new Date(Math.max(r.getTime(),i)),s=new Date(Math.min(s.getTime(),a)),e=null}else e=s=r=t;p(r,s);const i=a(),c=f(i.search.slice(1),{from:r,to:s,org:o});c.append("tab","overview"),i.search=c.toString(),d(i.toString())}(j(r),t.shiftKey,o)}));const u=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];async function d(e){const t=document.getElementById("js-contribution-activity");if(!t)return;t.classList.add("loading");const n=await i(document,e);t.classList.remove("loading"),t.innerHTML="",t.append(n)}function f(e,t){const n=new URLSearchParams(e);n.delete("from"),n.delete("to"),n.delete("org");let o=t.fromStr;t.from&&(o=w(t.from)),o&&n.append("from",o);let r=t.toStr;t.to&&(r=w(t.to)),r&&n.append("to",r);const s=t.org;return s&&n.append("org",s),n}async function m(e,t,n){const o=document.querySelector(".js-calendar-graph").getAttribute("data-graph-url"),r=new URL(o,window.location.origin),s=f(r.search.slice(1),{from:e,to:t,org:n});r.search=s.toString();const a=await i(document,r.toString());document.querySelector(".js-yearly-contributions").replaceWith(a)}function p(e,t){const n=document.querySelector(".js-calendar-graph"),o=n.querySelectorAll("rect.day");for(const s of o)s.classList.remove("active");if(n.classList.remove("days-selected"),e||t){n.classList.add("days-selected");for(const e of o)r(e)&&e.classList.add("active")}function r(n){const o=j(n.getAttribute("data-date")||"").getTime();return e&&t?e.getTime()<=o&&o<=t.getTime():e?o===e.getTime():void 0}}function g(){const e=document.querySelector(".js-calendar-graph").querySelectorAll("rect.active"),t=e[0],n=e[e.length-1],o=t&&t.getAttribute("data-date"),r=n&&n.getAttribute("data-date");return o&&r?{first:o,last:r}:null}function h(){return g()||function(){const e=new URLSearchParams(window.location.search.slice(1)),t=e.get("from"),n=e.get("to");return t&&n?{first:t,last:n}:null}()||function(){const e=new URL(S(),window.location.origin),t=new URLSearchParams(e.search.slice(1)),n=t.get("from"),o=t.get("to");return n&&o?{first:n,last:o}:null}()}function y(e){return("0"+e).slice(-2)}function w(e){return`${e.getUTCFullYear()}-${y(e.getUTCMonth()+1)}-${y(e.getUTCDate())}`}function j(e){const[t,n,o]=e.split("-").map((e=>parseInt(e,10)));return new Date(Date.UTC(t,n-1,o))}async function b(e){const t=g(),n=function(){const e=document.querySelector(".js-calendar-graph");return{first:e.getAttribute("data-from"),last:e.getAttribute("data-to")}}(),o=new Date(n.first),r=new Date(n.last);if(await m(o,r,e),t){p(new Date(t.first),new Date(t.last))}}function S(){return document.querySelector(".js-profile-timeline-year-list .js-year-link.selected").href||""}function v(e){const t=new URL(e,window.location.origin).search,n=new URLSearchParams(t.slice(1)),o=n.get("org"),r=n.get("from"),s=n.get("to"),i=new Date(r),c=new Date(s);m(i,c,o);const l=a(),u=f(l.search.slice(1),{from:i,to:c,org:o});u.append("tab","overview"),l.search=u.toString(),d(l.toString())}function L(e){const t=e.closest(".js-details-container");t&&t.classList.add("open");const n=e.getBoundingClientRect(),o=window.scrollY+n.top-62-10;window.scrollTo(0,o)}function q(e){document.querySelector(".js-profile-editable-area").hidden=e,document.querySelector(".js-profile-editable-form").hidden=!e,document.querySelector(".js-profile-editable-error").textContent=""}n("click",".js-org-filter-link",(function(e){e.stopPropagation(),e.preventDefault();const t=e.currentTarget,n=t.closest(".js-org-filter-links-container").querySelector(".js-org-filter-link.selected"),o=new URL(t.href,window.location.origin),r=new URLSearchParams(o.search.slice(1)),c=r.get("org"),l=h(),u=new Date(l.first),m=new Date(l.last);n&&n.classList.remove("selected"),t!==n&&t.classList.add("selected"),b(c);const p=a(),g={org:c,from:null,to:null};r.has("from")&&(g.from=u),r.has("to")&&(g.to=m);const y=f(p.search.slice(1),g);p.search=y.toString(),d(p.toString()),async function(e,t){const n=document.getElementById("year-list-container");if(!n)return;t.append("year_list","1"),e.search=t.toString();const o=await i(document,e.toString());n.innerHTML="",n.append(o)}(p,y),s(null,"",p.toString())})),n("click",".js-year-link",(function(e){e.stopPropagation(),e.preventDefault();const t=e.currentTarget;t.closest("ul").querySelector(".js-year-link.selected").classList.remove("selected"),t.classList.add("selected"),v(t.href),s(null,"",t.href)})),function(){const e=window.location.hash;if(!e||e.indexOf("#event-")<0)return;const t=e.slice(1,e.length),n=document.getElementById(t);n&&L(n)}(),window.addEventListener("hashchange",(function(e){const t=e.newURL||window.location.href,n=t.slice(t.indexOf("#")+1,t.length),o=document.getElementById(n);o&&(e.stopPropagation(),L(o))})),r(".js-show-more-timeline-form",(async function(e,t){await t.text();const n=document.querySelector(".js-show-more-timeline-form");if(n){const t=n.getAttribute("data-year"),o=document.querySelector(".js-year-link.selected"),r=document.querySelector("#year-link-"+t);o.classList.remove("selected"),r.classList.add("selected");if(t!==e.getAttribute("data-year")){const e=n.getAttribute("data-from"),t=new Date(e),o=n.getAttribute("data-to");m(t,new Date(o),n.getAttribute("data-org"))}}document.title=e.getAttribute("data-title")||"",s(null,"",e.getAttribute("data-url")||"")})),o(".js-activity-overview-graph-container",(e=>{!async function(e){const{initializeOverviewGraphContainer:n}=await t.import("./chunk-contributions-spider-graph.js");n(e)}(e)})),n("click",".js-profile-editable-edit-button",(function(){!function(){const e=document.querySelector(".js-user-profile-bio").textContent;if("string"!=typeof e)return;document.querySelector(".js-user-profile-bio-edit").value=e}(),q(!0)})),n("click",".js-profile-editable-cancel",(function(){q(!1)})),r(".js-profile-editable-form",(async(e,t)=>{let n;try{n=await t.html()}catch(r){if(422===r.response.status){document.querySelector(".js-profile-editable-error").textContent=r.response.json.message}return}var o;o=n.html,document.querySelector(".js-profile-editable-area").replaceWith(o),q(!1)}));let k=null,A=null;function C(e){const{item:t,oldIndex:n}=e,{parentNode:o}=t;A=o.children[n+1]}async function x(e){const{oldIndex:t,newIndex:n,item:o}=e;if(t===n)return;const r=o.closest(".js-pinned-items-reorder-form"),s=r.closest(".js-pinned-items-reorder-container"),i=s.querySelector(".js-pinned-items-spinner"),a=s.querySelector(".js-pinned-items-reorder-message");a.textContent="",i.style.display="inline-block",k.option("disabled",!0);if((await fetch(r.action,{method:r.method,body:new FormData(r),headers:{"X-Requested-With":"XMLHttpRequest"}})).ok)a.textContent=a.getAttribute("data-success-text")||"",i.style.display="none",k.option("disabled",!1);else{a.textContent=a.getAttribute("data-error-text")||"",i.style.display="none";const e=o.parentNode;A?e.insertBefore(o,A):e.appendChild(o)}}function T(e,t){t>0?(e.textContent=function(e){return e>999?(e/1e3).toFixed(1)+"k":e.toLocaleString()}(t),e.hidden=!1):e.remove()}o(".js-pinned-items-reorder-list",{async add(e){const{Sortable:n}=await t.import("./chunk-sortable-behavior.js");k=n.create(e,{animation:150,item:".js-pinned-item-list-item",handle:".js-pinned-item-reorder",onUpdate:x,onStart:C,chosenClass:"is-dragging"})}}),n("submit",".js-pinned-items-reorder-form",(function(e){e.preventDefault()})),n("click",".js-pinned-item-list-item .js-sortable-button",(async function({currentTarget:e}){const{moveWithButton:n}=await t.import("./chunk-sortable-behavior.js");n(e,e.closest(".js-pinned-item-list-item"),x)})),n("click",".js-pinned-items-dialog",(()=>{t.import("./chunk-profile-pins-element.js")})),o(".js-user-profile-sticky-fields.is-stuck",(function(){const e=document.querySelector(".js-user-profile-sticky-bar");return{add(){e.classList.add("is-stuck")},remove(){e.classList.remove("is-stuck")}}})),o(".js-user-profile-follow-button.is-stuck",(function(){const e=document.querySelector(".js-user-profile-sticky-bar");return{add(){e.classList.add("is-follow-stuck")},remove(){e.classList.remove("is-follow-stuck")}}})),o(".js-profile-tab-count-container",(function(e){!async function(e){const t=new URL(e.getAttribute("data-url"),window.location.origin),n=new URLSearchParams(t.search.slice(1)),o=e.querySelector(".js-profile-repository-count"),r=e.querySelector(".js-profile-project-count"),s=e.querySelector(".js-profile-team-count"),i=e.querySelector(".js-profile-member-count");o&&n.append("repo","1"),r&&n.append("project","1"),s&&n.append("team","1"),i&&n.append("member","1"),t.search=n.toString();const a=await fetch(t.toString(),{headers:{"X-Requested-With":"XMLHttpRequest"}});if(!a.ok)return;const c=(await a.json()).data;o&&c.repositories&&T(o,c.repositories.totalCount),r&&c.projects&&T(r,c.projects.totalCount),s&&c.teams&&T(s,c.teams.totalCount),i&&c.members&&T(i,c.members.totalCount)}(e)}))}}}));
//# sourceMappingURL=profile-a7350fa8.js.map
