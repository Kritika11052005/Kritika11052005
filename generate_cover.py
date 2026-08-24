import base64
import urllib.request
import json
import re

# Fetch latest live metrics directly
try:
    req = urllib.request.Request('https://github-contributions-api.jogruber.de/v4/Kritika11052005?y=last', headers={'User-Agent': 'Mozilla/5.0'})
    data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    yearly_contributions = data.get('total', {}).get('lastYear', 689)
except Exception as e:
    yearly_contributions = 689

try:
    req = urllib.request.Request('https://komarev.com/ghpvc/?username=Kritika11052005', headers={'User-Agent': 'Mozilla/5.0'})
    svg_raw = urllib.request.urlopen(req).read().decode('utf-8')
    nums = re.findall(r'>(\d+)<', svg_raw)
    profile_views = nums[-1] if nums else "775"
except Exception as e:
    profile_views = "775"

with open("placeholder-user1.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")

svg_content = f"""<svg width="100%" height="100%" viewBox="0 0 900 860" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,600;1,700;1,900&amp;family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600;1,700&amp;family=Inter:wght@300;400;500;600;700&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap');

      .masthead-first {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 66px;
        font-weight: 900;
        letter-spacing: 14px;
        fill: #FAFAF9;
        text-transform: uppercase;
      }}
      .masthead-last {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 62px;
        font-weight: 400;
        font-style: italic;
        letter-spacing: 8px;
        fill: #D4A574;
        text-transform: uppercase;
      }}
      .tagline {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 15.5px;
        font-style: italic;
        letter-spacing: 1.5px;
        fill: #D4A574;
      }}
      .category {{
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 3.5px;
        fill: #D97706;
        text-transform: uppercase;
      }}
      .article-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 15.5px;
        font-weight: 600;
        fill: #F5F5F4;
        line-height: 1.25;
      }}
      .article-title-italic {{
        font-style: italic;
        fill: #D4A574;
      }}
      .article-sub {{
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 11px;
        font-weight: 400;
        fill: #A8A29E;
        line-height: 1.4;
      }}
      .side-text {{
        font-family: 'Inter', sans-serif;
        font-size: 8px;
        letter-spacing: 6px;
        fill: #44403C;
        text-transform: uppercase;
      }}
      .barcode-text {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 8px;
        letter-spacing: 2px;
        fill: #57534E;
      }}
      .ticker-text {{
        font-family: 'JetBrains Mono', 'Courier New', monospace;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1.5px;
        fill: #FCD34D;
      }}
    </style>

    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="860" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#08080A"/>
      <stop offset="40%" stop-color="#0C0C12"/>
      <stop offset="100%" stop-color="#11121A"/>
    </linearGradient>

    <!-- Gold Accent Line -->
    <linearGradient id="goldBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#B45309"/>
      <stop offset="25%" stop-color="#D97706"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="75%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>

    <!-- Photo Bottom Dissolve Gradient -->
    <linearGradient id="fadeBottom" x1="0" y1="480" x2="0" y2="720" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0C0C12" stop-opacity="0"/>
      <stop offset="40%" stop-color="#0C0C12" stop-opacity="0.5"/>
      <stop offset="80%" stop-color="#0C0C12" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0C0C12" stop-opacity="1"/>
    </linearGradient>

    <!-- Luxury Badge Gradients -->
    <linearGradient id="viewsBadgeBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#181512"/>
      <stop offset="100%" stop-color="#0E0C0A"/>
    </linearGradient>

    <linearGradient id="contribBadgeBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0B131E"/>
      <stop offset="100%" stop-color="#080C14"/>
    </linearGradient>

    <clipPath id="coverClip">
      <rect width="900" height="860" rx="4"/>
    </clipPath>

    <!-- Typewriter Reveal Masks -->
    <clipPath id="typewriterTagline">
      <rect x="-350" y="10" width="0" height="40">
        <animate attributeName="width" from="0" to="700" dur="1.4s" begin="0.6s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1" />
      </rect>
    </clipPath>

    <clipPath id="typewriterLeft1">
      <rect x="0" y="-20" width="0" height="90">
        <animate attributeName="width" from="0" to="300" dur="0.9s" begin="0.9s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>

    <clipPath id="typewriterLeft2">
      <rect x="0" y="-20" width="0" height="90">
        <animate attributeName="width" from="0" to="300" dur="0.9s" begin="1.2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>

    <clipPath id="typewriterLeft3">
      <rect x="0" y="-20" width="0" height="180">
        <animate attributeName="width" from="0" to="350" dur="1.2s" begin="1.5s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>

    <clipPath id="typewriterRight1">
      <rect x="-300" y="-20" width="0" height="110">
        <animate attributeName="width" from="0" to="320" dur="0.9s" begin="1.0s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>

    <clipPath id="typewriterRight2">
      <rect x="-300" y="-20" width="0" height="120">
        <animate attributeName="width" from="0" to="320" dur="0.9s" begin="1.3s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>

    <clipPath id="typewriterRight3">
      <rect x="-300" y="-20" width="0" height="130">
        <animate attributeName="width" from="0" to="320" dur="0.9s" begin="1.6s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>
  </defs>

  <g clip-path="url(#coverClip)">
    <!-- Canvas Background -->
    <rect width="900" height="860" fill="url(#bgGrad)"/>

    <!-- Subtle Linen Grid -->
    <g opacity="0.025" stroke="#FFFFFF" stroke-width="0.5">
      <line x1="0" y1="120" x2="900" y2="120"/>
      <line x1="0" y1="240" x2="900" y2="240"/>
      <line x1="0" y1="360" x2="900" y2="360"/>
      <line x1="0" y1="480" x2="900" y2="480"/>
      <line x1="0" y1="600" x2="900" y2="600"/>
      <line x1="0" y1="720" x2="900" y2="720"/>
    </g>

    <!-- Top Gold Luxury Strip -->
    <rect x="0" y="0" width="900" height="5" fill="url(#goldBar)">
      <animate attributeName="opacity" from="0" to="1" dur="0.8s" fill="freeze"/>
    </rect>

    <!-- Outer Frame Borders -->
    <rect x="14" y="14" width="872" height="832" fill="none" stroke="#292524" stroke-width="0.8" opacity="0.6"/>
    <rect x="18" y="18" width="864" height="824" fill="none" stroke="#44403C" stroke-width="0.4" opacity="0.3"/>

    <!-- ═══════ CENTERPIECE PORTRAIT PHOTO (LOWERED ACCORDINGLY FOR LUXURIOUS CLEARANCE) ═══════ -->
    <g transform="translate(170, 118)" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="1.2s" begin="0.2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.16 1 0.3 1"/>
      <animateTransform attributeName="transform" type="translate" from="170, 144" to="170, 118" dur="1.2s" begin="0.2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.16 1 0.3 1"/>
      
      <image href="data:image/png;base64,{img_b64}" x="0" y="0" width="560" height="660" preserveAspectRatio="xMidYMid meet" />
      <rect x="0" y="420" width="560" height="240" fill="url(#fadeBottom)" />
    </g>

    <!-- ═══════ MASTHEAD (SHIFTED LOWER WITH COMFORTABLE TOP MARGIN) ═══════ -->
    <g transform="translate(450, 68)" text-anchor="middle">
      <g opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="0.1s" fill="freeze"/>
        <text y="0">
          <tspan class="masthead-first">KRITIKA</tspan>
          <tspan dx="16" class="masthead-last">BENJWAL</tspan>
        </text>
        <line x1="-340" y1="14" x2="340" y2="14" stroke="url(#goldBar)" stroke-width="1.2" opacity="0.9"/>
      </g>

      <!-- Tagline with Typewriter Reveal Effect -->
      <g clip-path="url(#typewriterTagline)">
        <text y="34" class="tagline">"Building AI that thinks, systems that scale, and research that matters."</text>
      </g>
    </g>

    <!-- ═══════ LEFT COLUMN: EDITORIAL COVER LINES ═══════ -->
    <g transform="translate(42, 230)">
      
      <!-- Section 1: EDUCATION -->
      <g transform="translate(0, 0)" clip-path="url(#typewriterLeft1)">
        <text class="category">EDUCATION &amp; FOCUS</text>
        <text y="22" class="article-title">B.Tech <tspan class="article-title-italic">CSE</tspan> @ MUJ '27</text>
        <text y="39" class="article-sub">Manipal University Jaipur · Rajasthan</text>
        <line x1="0" y1="52" x2="190" y2="52" stroke="#292524" stroke-width="0.8"/>
      </g>

      <!-- Section 2: LIVE PROFILE VIEWS -->
      <g transform="translate(0, 72)" clip-path="url(#typewriterLeft2)">
        <text class="category">LIVE PROFILE VIEWS</text>
        
        <g transform="translate(0, 8)">
          <rect width="170" height="26" rx="4" fill="url(#viewsBadgeBg)" stroke="#D97706" stroke-width="1"/>
          <line x1="108" y1="0" x2="108" y2="26" stroke="#D97706" stroke-width="0.8" opacity="0.6"/>
          
          <circle cx="12" cy="13" r="3.5" fill="#D97706">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
          </circle>
          
          <text x="22" y="17" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#E7E5E4" letter-spacing="1">
            VIEWS
          </text>
          
          <text x="139" y="17" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#F59E0B" text-anchor="middle" letter-spacing="0.5">
            {profile_views}
          </text>
        </g>
        
        <text y="48" class="article-sub">Real-Time Traffic Counter</text>
        <line x1="0" y1="62" x2="190" y2="62" stroke="#292524" stroke-width="0.8"/>
      </g>

      <!-- Section 3: RECOGNITION & IMPACT -->
      <g transform="translate(0, 154)" clip-path="url(#typewriterLeft3)">
        <text class="category">RECOGNITION &amp; IMPACT</text>
        
        <circle cx="4" cy="18" r="2.5" fill="#D97706"/>
        <text x="14" y="22" class="article-title" font-size="14px">Open Source Contributor</text>
        <text x="14" y="37" class="article-sub">Hacktoberfest &amp; GSSoC '25</text>
        
        <circle cx="4" cy="58" r="2.5" fill="#D97706"/>
        <text x="14" y="62" class="article-title" font-size="14px">AI for Good <tspan class="article-title-italic">Winner</tspan></text>
        <text x="14" y="77" class="article-sub">India Consolation Prize Winner</text>

        <circle cx="4" cy="98" r="2.5" fill="#D97706"/>
        <text x="14" y="102" class="article-title" font-size="13.5px">India AI Impact Buildathon Finalist</text>
        <text x="14" y="117" class="article-sub">Top 2% amongst 40,000+ participants</text>
      </g>

    </g>

    <!-- ═══════ RIGHT COLUMN: EDITORIAL COVER LINES ═══════ -->
    <g transform="translate(858, 230)" text-anchor="end">
      
      <!-- Section 1: LIVE GITHUB CONTRIBUTIONS -->
      <g transform="translate(0, 0)" clip-path="url(#typewriterRight1)">
        <text class="category">LIVE GITHUB CONTRIBUTIONS</text>
        <text y="22" class="article-title">Past 1-Year <tspan class="article-title-italic">Activity</tspan></text>
        
        <g transform="translate(-195, 30)">
          <rect width="195" height="26" rx="4" fill="url(#contribBadgeBg)" stroke="#38BDF8" stroke-width="1"/>
          <line x1="135" y1="0" x2="135" y2="26" stroke="#38BDF8" stroke-width="0.8" opacity="0.6"/>
          
          <circle cx="12" cy="13" r="3.5" fill="#38BDF8">
            <animate attributeName="opacity" values="1;0.3;1" dur="1.6s" repeatCount="indefinite"/>
          </circle>
          
          <text x="22" y="17" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#E0F2FE" text-anchor="start" letter-spacing="1">
            YEARLY COMMITS
          </text>
          
          <text x="165" y="17" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#38BDF8" text-anchor="middle" letter-spacing="0.5">
            {yearly_contributions}
          </text>
        </g>
        
        <text y="72" class="article-sub">Verified Past 365 Days on GitHub</text>
        <line x1="-195" y1="86" x2="0" y2="86" stroke="#292524" stroke-width="0.8"/>
      </g>

      <!-- Section 2: EDITORIAL PROFILE -->
      <g transform="translate(0, 104)" clip-path="url(#typewriterRight2)">
        <text class="category">EDITORIAL PROFILE</text>
        <text y="22" class="article-title">The Engineer Building</text>
        <text y="42" class="article-title"><tspan class="article-title-italic">Intelligent</tspan> Systems</text>
        <text y="62" class="article-sub">Intersection of Fullstack and AI/ML</text>
        <line x1="-195" y1="76" x2="0" y2="76" stroke="#292524" stroke-width="0.8"/>
      </g>

      <!-- Section 3: BARCODE & ISSUE DETAILS -->
      <g transform="translate(0, 204)" clip-path="url(#typewriterRight3)">
        <text class="category">ISSUE &amp; VERIFICATION</text>
        <g transform="translate(-120, 16)">
          <g fill="#3E3835">
            <rect x="0" y="0" width="2.5" height="34"/>
            <rect x="5" y="0" width="1.5" height="34"/>
            <rect x="9" y="0" width="3.5" height="34"/>
            <rect x="15" y="0" width="1.5" height="34"/>
            <rect x="18" y="0" width="2" height="34"/>
            <rect x="23" y="0" width="4" height="34"/>
            <rect x="29" y="0" width="1.5" height="34"/>
            <rect x="33" y="0" width="3" height="34"/>
            <rect x="38" y="0" width="1.5" height="34"/>
            <rect x="42" y="0" width="2.5" height="34"/>
            <rect x="47" y="0" width="4.5" height="34"/>
            <rect x="54" y="0" width="1.5" height="34"/>
            <rect x="58" y="0" width="3" height="34"/>
            <rect x="63" y="0" width="2" height="34"/>
            <rect x="68" y="0" width="3.5" height="34"/>
            <rect x="74" y="0" width="1.5" height="34"/>
            <rect x="78" y="0" width="2.5" height="34"/>
            <rect x="83" y="0" width="3" height="34"/>
            <rect x="88" y="0" width="2" height="34"/>
            <rect x="93" y="0" width="3" height="34"/>
            <rect x="98" y="0" width="1.5" height="34"/>
            <rect x="103" y="0" width="3.5" height="34"/>
            <rect x="109" y="0" width="2" height="34"/>
            <rect x="114" y="0" width="3" height="34"/>
          </g>
        </g>
        <text y="66" class="barcode-text">ISSUE N° 2027 · JAIPUR</text>
        <text y="80" class="barcode-text" fill="#78716C">github.com/Kritika11052005</text>
      </g>

    </g>

    <!-- ═══════ BELOW PHOTO: TYPEWRITER LIVE TICKER ═══════ -->
    <g transform="translate(450, 755)" text-anchor="middle">
      <g opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="1.2s" fill="freeze"/>
        
        <!-- Luxury Badge Pill Bar -->
        <rect x="-380" y="-22" width="760" height="44" rx="22" fill="#0C0A09" stroke="url(#goldBar)" stroke-width="1.2"/>
        
        <!-- Pulsing Indicator Dots -->
        <circle cx="-352" cy="0" r="4" fill="#D97706">
          <animate attributeName="opacity" values="0.4;1;0.4" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <circle cx="352" cy="0" r="4" fill="#F59E0B">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>

        <!-- Slide 1: Fullstack development -->
        <g opacity="0">
          <text y="5" class="ticker-text">
            <tspan fill="#F59E0B">✦</tspan> FULLSTACK DEVELOPMENT <tspan fill="#F59E0B">✦</tspan>
          </text>
          <animate attributeName="opacity" values="1;1;0;0;0;0;0;0;1" keyTimes="0;0.21;0.25;0.50;0.54;0.75;0.79;0.96;1" dur="12s" repeatCount="indefinite"/>
        </g>

        <!-- Slide 2: AI/ML Engineering and Research -->
        <g opacity="0">
          <text y="5" class="ticker-text">
            <tspan fill="#38BDF8">✦</tspan> AI/ML ENGINEERING AND RESEARCH <tspan fill="#38BDF8">✦</tspan>
          </text>
          <animate attributeName="opacity" values="0;0;1;1;0;0;0;0;0" keyTimes="0;0.21;0.25;0.46;0.50;0.75;0.79;0.96;1" dur="12s" repeatCount="indefinite"/>
        </g>

        <!-- Slide 3: Software Engineering -->
        <g opacity="0">
          <text y="5" class="ticker-text">
            <tspan fill="#A855F7">✦</tspan> SOFTWARE ENGINEERING <tspan fill="#A855F7">✦</tspan>
          </text>
          <animate attributeName="opacity" values="0;0;0;0;1;1;0;0;0" keyTimes="0;0.21;0.25;0.46;0.50;0.71;0.75;0.96;1" dur="12s" repeatCount="indefinite"/>
        </g>

        <!-- Slide 4: Building Intelligent platforms and systems -->
        <g opacity="0">
          <text y="5" class="ticker-text">
            <tspan fill="#10B981">✦</tspan> BUILDING INTELLIGENT PLATFORMS AND SYSTEMS <tspan fill="#10B981">✦</tspan>
          </text>
          <animate attributeName="opacity" values="0;0;0;0;0;0;1;1;0" keyTimes="0;0.21;0.25;0.46;0.50;0.71;0.75;0.96;1" dur="12s" repeatCount="indefinite"/>
        </g>
      </g>
    </g>

    <!-- Side Vertical Text -->
    <g transform="translate(18, 430) rotate(-90)">
      <text class="side-text" text-anchor="middle">GITHUB · KRITIKA11052005 · PORTFOLIO 2026</text>
    </g>
    <g transform="translate(882, 430) rotate(90)">
      <text class="side-text" text-anchor="middle">COMPUTER SCIENCE &amp; ENGINEERING · MUJ '27</text>
    </g>

    <!-- Bottom Luxury Border -->
    <rect x="0" y="855" width="900" height="5" fill="#1C1917"/>
    <rect x="0" y="855" width="300" height="5" fill="url(#goldBar)"/>
  </g>
</svg>
"""

with open("tech-vogue.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Shifted KRITIKA BENJWAL lower with clean top margin. Views: {profile_views}, Commits: {yearly_contributions}")
