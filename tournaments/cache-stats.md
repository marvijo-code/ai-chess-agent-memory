# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 165 | 1687987 | 832256 | 49.3% | 49.4% |
| GPT-6.1 Sol | 150 | 4725159 | 4478592 | 94.8% | 95.1% |
| Sonnet 5.5 | 132 | 2823655 | 2693648 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3479 | 37727922 | 17395968 | 46.1% | 46.0% |
| GPT-6.1 Sol | 3050 | 89498842 | 83151232 | 92.9% | 93.4% |
| Sonnet 5.5 | 3219 | 72213783 | 69021792 | 95.6% | 96.2% |
