# 🃏 DeckForge - 輕量級AI驅動PPT智慧生成CLI引擎

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)]()

> ⚡ 在終端中將任何內容轉化為專業、原生可編輯的PowerPoint簡報——無需AI IDE。

**[简体中文](README_zh.md)** | **繁體中文** | **[English](README.md)**

---

## 🎉 專案介紹

**DeckForge** 是一款輕量級CLI引擎，利用大型語言模型（LLM）直接在終端中生成專業、原生可編輯的 `.pptx` 檔案。與其他需要Claude Code或Cursor等AI IDE的簡報工具不同，DeckForge作為**獨立的命令列工具**運作——只需提供內容，即可獲得精美的簡報。

### 💡 靈感來源

受GitHub上AI驅動簡報工具熱潮的啟發，DeckForge誕生於對**零依賴、無需IDE**解決方案的需求。大多數現有工具將你鎖定在特定的AI IDE或雲端平台上。DeckForge打破了這些限制——純CLI，純自由。

### 🌟 差異化亮點

| 特性 | DeckForge | 其他工具 |
|------|-----------|----------|
| 🖥️ 需要AI IDE | ❌ 不需要 | ✅ 需要（Claude Code、Cursor等） |
| ⌨️ 獨立CLI | ✅ 支援 | ❌ 不支援 |
| 🤖 多LLM後端 | ✅ OpenAI、Claude、DeepSeek、Ollama | 有限 |
| 📦 核心依賴 | **1個**（python-pptx） | 很多 |
| 🎨 內建主題 | ✅ **11款專業主題** | 僅外部 |
| 🔒 離線模式 | ✅ 純模板模式 | ❌ 不支援 |
| 🌍 多語言 | ✅ 內容自動偵測 | 有限 |
| 💰 費用 | 免費開源 | 通常付費 |

---

## ✨ 核心特性

- 🚀 **一鍵生成** — 單條CLI命令即可生成簡報
- 🤖 **多LLM後端** — 支援OpenAI、Claude、DeepSeek和Ollama（本地）
- 🎨 **11款內建主題** — 現代、暗黑、學術、極簡、海洋、自然、日落、科技、商務、創意、翡翠
- 📝 **智慧內容解析** — 自動將Markdown和純文字解析為幻燈片結構
- 🔧 **純模板模式** — 無需任何API金鑰即可生成精美簡報（`--no-ai`）
- 📊 **原生PPTX輸出** — 真實的PowerPoint形狀、文字方塊和版面配置（非圖片）
- 🌐 **多語言支援** — 自動偵測內容語言，支援中/英/日/韓等
- 🧩 **模組化架構** — 可插拔的解析器、渲染器和LLM後端
- 🧪 **充分測試** — 25+單元測試覆蓋所有核心模組
- 📦 **零核心依賴** — 僅需 `python-pptx` 作為執行期依賴

---

## 🚀 快速開始

### 📋 環境需求

- **Python 3.10+** — 唯一必要條件
- **python-pptx** — 透過requirements.txt自動安裝

### 🔧 安裝

```bash
# 複製倉庫
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge

# 安裝依賴
pip install -r requirements.txt

# 或安裝為CLI工具
pip install -e .
```

### ⚡ 基本用法

```bash
# 從內聯文字生成
deckforge create --input "機器學習入門" --output slides.pptx

# 從Markdown檔案生成
deckforge create --input content.md --output presentation.pptx

# 使用指定主題生成
deckforge create --input content.md --theme dark --output dark_slides.pptx

# 無AI模式生成（純模板模式）
deckforge create --input content.md --no-ai --output template.pptx

# 列出所有可用主題
deckforge themes

# 顯示詳細主題資訊
deckforge themes --detail

# 查看環境和API金鑰狀態
deckforge info
```

### 🔑 LLM配置

```bash
# 設定你偏好的LLM API金鑰
export OPENAI_API_KEY="sk-your-key-here"
# 或
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
# 或
export DEEPSEEK_API_KEY="sk-your-key-here"

# 對於Ollama（本地），確保它正在執行：
ollama serve
```

---

## 📖 詳細使用指南

### 🎨 主題一覽

DeckForge內建11款專業設計主題：

| 主題 | 風格 | 適用場景 |
|------|------|----------|
| 🃏 `modern` | 簡潔藍色調 | 通用場景 |
| 🌙 `dark` | 優雅暗色背景 | 技術簡報 |
| 🎓 `academic` | 正式襯線字型 | 學術研究 |
| ⬜ `minimal` | 極致留白 | 設計導向 |
| 🌊 `ocean` | 深海藍色調 | 科技創業 |
| 🌿 `nature` | 溫暖大地色調 | 環保健康 |
| 🌅 `sunset` | 暖色漸層 | 創意展示 |
| 💻 `tech` | 未來科技感 | 創業路演 |
| 💼 `business` | 商務專業風 | 商務會議 |
| 🎨 `creative` | 大膽藝術色 | 創意作品集 |
| 💚 `emerald` | 翡翠綠色調 | 高端活動 |

### 📝 輸入格式

#### Markdown輸入（推薦）

```markdown
# 簡報標題

## 簡介

這裡是簡介內容。

## 核心特性

- 特性一，支援**粗體文字**
- 特性二，支援*斜體文字*
- 特性三

## 程式碼範例

\`\`\`python
def hello():
    print("你好，世界！")
\`\`\`
```

#### 純文字輸入

```
機器學習概述

機器學習正在改變全球各行各業。

主要應用包括：
- 自然語言處理
- 電腦視覺
- 自動駕駛
```

### 🤖 LLM增強功能

配置LLM後端後，DeckForge會自動增強你的內容：

1. **標題最佳化** — 使標題更具吸引力和針對性
2. **要點精煉** — 提升要點的簡潔性和影響力
3. **演講備註** — 為每張幻燈片生成有用的備註
4. **流程最佳化** — 確保幻燈片之間的邏輯連貫性

### ⌨️ CLI參考

```
deckforge create [選項]

選項:
  -i, --input TEXT     輸入內容：文字字串或檔案路徑  [必需]
  -o, --output TEXT    輸出PPTX檔案路徑  [預設: output.pptx]
  -t, --theme TEXT     主題名稱  [預設: modern]
  --llm TEXT           LLM後端: openai|claude|deepseek|ollama|none  [預設: openai]
  --model TEXT         指定模型名稱覆蓋
  --slides INTEGER     目標幻燈片數量
  --lang TEXT          語言: en|zh|ja|ko|auto  [預設: auto]
  --title TEXT         自訂簡報標題
  --no-ai             無LLM生成（純模板模式）
```

---

## 💡 設計思路與迭代規劃

### 🎯 設計理念

1. **簡潔優先** — 一條命令生成，零配置需求
2. **無鎖定** — 無AI IDE依賴，無雲端平台鎖定
3. **模組化架構** — 每個元件都可插拔和替換
4. **離線可用** — 純模板模式無需任何API
5. **原生輸出** — 真實的PowerPoint元素，非扁平化圖片

### 🗺️ 迭代規劃

- [ ] **v1.1** — 模板自訂（自訂顏色、字型、版面配置）
- [ ] **v1.2** — 圖片插入支援（本地檔案和AI生成）
- [ ] **v1.3** — 圖表生成（長條圖、圓餅圖、折線圖）
- [ ] **v1.4** — 互動式幻燈片過渡和動畫
- [ ] **v2.0** — Web UI視覺化編輯
- [ ] **v2.1** — 外掛系統，支援社群主題和渲染器

---

## 📦 打包與部署指南

### 從原始碼安裝

```bash
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge
pip install -r requirements.txt
```

### 作為Python套件安裝

```bash
pip install git+https://github.com/gitstq/DeckForge.git
```

### 開發模式

```bash
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge
pip install -e ".[dev]"
pytest  # 執行測試
```

### 🖥️ 相容環境

| 平台 | Python 3.10 | Python 3.11 | Python 3.12 | Python 3.13 |
|------|:-----------:|:-----------:|:-----------:|:-----------:|
| 🪟 Windows | ✅ | ✅ | ✅ | ✅ |
| 🍎 macOS | ✅ | ✅ | ✅ | ✅ |
| 🐧 Linux | ✅ | ✅ | ✅ | ✅ |

---

## 🤝 貢獻指南

歡迎貢獻！請遵循以下指南：

1. 🍴 Fork本倉庫
2. 🌿 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 💾 提交變更 (`git commit -m 'feat: 新增功能'`)
4. 📤 推送分支 (`git push origin feature/amazing-feature`)
5. 🎉 發起Pull Request

### 提交規範

我們遵循 [Conventional Commits](https://www.conventionalcommits.org/) 規範：

- `feat:` 新功能
- `fix:` Bug修復
- `docs:` 文件更新
- `refactor:` 程式碼重構
- `test:` 測試新增/更新
- `chore:` 維護任務

---

## 📄 開源授權

本專案基於 **MIT授權** 開源——詳見 [LICENSE](LICENSE) 檔案。

---

<p align="center">
  由 DeckForge Team 用 ❤️ 打造<br>
  <sub>一條命令，將你的想法變為簡報。</sub>
</p>
