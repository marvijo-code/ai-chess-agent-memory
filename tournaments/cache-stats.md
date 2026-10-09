# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 231 | 2709749 | 1222528 | 45.1% | 45.1% |
| GPT-6.1 Sol | 174 | 4902166 | 4526336 | 92.3% | 92.9% |
| Sonnet 5.5 | 168 | 3392778 | 3223187 | 95.0% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1935 | 21789283 | 10056704 | 46.2% | 46.1% |
| GPT-6.1 Sol | 1548 | 45168865 | 42125696 | 93.3% | 93.7% |
| Sonnet 5.5 | 1710 | 39192980 | 37516798 | 95.7% | 96.2% |
