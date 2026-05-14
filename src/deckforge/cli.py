"""
DeckForge CLI - Main entry point
DeckForge CLI - 主入口
"""

import argparse
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def create_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog='deckforge',
        description='🃏 DeckForge - Lightweight AI-Powered PPT Intelligent Generation CLI Engine',
        epilog='Examples:\n'
               '  deckforge create --input "AI Overview" --output slides.pptx\n'
               '  deckforge create --input content.md --theme academic --output talk.pptx\n'
               '  deckforge themes\n'
               '  deckforge info',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # create command
    create_parser = subparsers.add_parser(
        'create',
        help='Generate a PPTX presentation from content',
        description='Generate a professional PPTX presentation from text, markdown, or file input.'
    )
    create_parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Input content: text string, markdown file path, or URL'
    )
    create_parser.add_argument(
        '-o', '--output',
        type=str,
        default='output.pptx',
        help='Output PPTX file path (default: output.pptx)'
    )
    create_parser.add_argument(
        '-t', '--theme',
        type=str,
        default='modern',
        help='Presentation theme (default: modern). Use "deckforge themes" to list all.'
    )
    create_parser.add_argument(
        '--llm',
        type=str,
        default='openai',
        choices=['openai', 'claude', 'deepseek', 'ollama', 'none'],
        help='LLM backend for content generation (default: openai). "none" for template-only mode.'
    )
    create_parser.add_argument(
        '--model',
        type=str,
        default=None,
        help='Specific model name (e.g., gpt-4o, claude-sonnet-4-20250514, deepseek-chat)'
    )
    create_parser.add_argument(
        '--slides',
        type=int,
        default=None,
        help='Target number of slides (default: auto-determined by LLM)'
    )
    create_parser.add_argument(
        '--lang',
        type=str,
        default='auto',
        help='Presentation language: en, zh, ja, ko, auto (default: auto-detect)'
    )
    create_parser.add_argument(
        '--title',
        type=str,
        default=None,
        help='Custom presentation title (default: extracted from content)'
    )
    create_parser.add_argument(
        '--no-ai',
        action='store_true',
        help='Generate from input without LLM enhancement (template-only mode)'
    )
    
    # themes command
    themes_parser = subparsers.add_parser(
        'themes',
        help='List all available presentation themes',
        description='Display all built-in presentation themes with previews.'
    )
    themes_parser.add_argument(
        '--detail',
        action='store_true',
        help='Show detailed theme information including color palettes'
    )
    
    # info command
    info_parser = subparsers.add_parser(
        'info',
        help='Show DeckForge configuration and environment info',
        description='Display current configuration, available LLM backends, and system info.'
    )
    
    # version
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'DeckForge v1.0.0'
    )
    
    return parser


def cmd_create(args: argparse.Namespace) -> int:
    """Handle the 'create' command."""
    from deckforge.engine import DeckForgeEngine
    
    # Resolve input
    input_path = args.input
    content = None
    
    if os.path.isfile(input_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"📄 Read input file: {input_path} ({len(content)} chars)")
    else:
        content = input_path
        print(f"📝 Using inline content: {len(content)} chars")
    
    # Determine LLM backend
    llm_backend = 'none' if args.no_ai else args.llm
    
    # Create engine
    engine = DeckForgeEngine(
        theme=args.theme,
        llm_backend=llm_backend,
        model=args.model,
        lang=args.lang,
        title=args.title,
        target_slides=args.slides
    )
    
    # Generate presentation
    print(f"\n🚀 Generating presentation...")
    print(f"   Theme: {args.theme}")
    print(f"   LLM: {llm_backend}")
    print(f"   Output: {args.output}")
    
    try:
        result = engine.create(content, args.output)
        print(f"\n✅ Presentation generated successfully!")
        print(f"   📁 File: {result}")
        print(f"   📊 Slides: {engine.slide_count}")
        return 0
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


def cmd_themes(args: argparse.Namespace) -> int:
    """Handle the 'themes' command."""
    from deckforge.themes.manager import ThemeManager
    
    manager = ThemeManager()
    themes = manager.list_themes()
    
    print("\n🎨 Available Themes\n" + "=" * 50)
    for theme in themes:
        info = manager.get_theme_info(theme)
        if args.detail:
            print(f"\n  📌 {theme}")
            print(f"     Description: {info.get('description', 'N/A')}")
            print(f"     Colors: {info.get('colors', 'N/A')}")
            print(f"     Font: {info.get('font', 'N/A')}")
        else:
            desc = info.get('description', '')
            print(f"  🃏 {theme:<12} - {desc}")
    
    print(f"\n  Total: {len(themes)} themes")
    return 0


def cmd_info(args: argparse.Namespace) -> int:
    """Handle the 'info' command."""
    import platform
    
    print("\n🃏 DeckForge Info\n" + "=" * 50)
    print(f"  Version:    1.0.0")
    print(f"  Python:     {platform.python_version()}")
    print(f"  Platform:   {platform.system()} {platform.release()}")
    print(f"  Architecture: {platform.machine()}")
    
    # Check dependencies
    try:
        import pptx
        print(f"  python-pptx: ✅ v{pptx.__version__}")
    except ImportError:
        print(f"  python-pptx: ❌ Not installed")
    
    # Check LLM API keys
    keys = {
        'OPENAI_API_KEY': os.environ.get('OPENAI_API_KEY'),
        'ANTHROPIC_API_KEY': os.environ.get('ANTHROPIC_API_KEY'),
        'DEEPSEEK_API_KEY': os.environ.get('DEEPSEEK_API_KEY'),
    }
    
    print(f"\n  🔑 API Keys:")
    for name, value in keys.items():
        status = "✅ Set" if value else "❌ Not set"
        print(f"     {name}: {status}")
    
    # Check Ollama
    import subprocess
    try:
        result = subprocess.run(['ollama', '--version'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"  🦙 Ollama: ✅ {result.stdout.strip()}")
        else:
            print(f"  🦙 Ollama: ❌ Not running")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print(f"  🦙 Ollama: ❌ Not installed")
    
    return 0


def main() -> int:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return 0
    
    if args.command == 'create':
        return cmd_create(args)
    elif args.command == 'themes':
        return cmd_themes(args)
    elif args.command == 'info':
        return cmd_info(args)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
