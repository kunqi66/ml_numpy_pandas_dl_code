import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def fetch_beijing_weather(year: int, month: int) -> pd.DataFrame:
    """爬取天气后报网北京历史天气，返回当月完整 DataFrame。"""
    url = f"http://www.tianqihoubao.com/lishi/beijing/month/{year}{month:02d}.html"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.encoding = "utf-8"

    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table", class_="weather-table")
    if table is None:
        raise RuntimeError(f"未找到天气表格，请检查页面: {url}")

    records = []
    for tr in table.find_all("tr")[1:]:  # 跳过表头
        tds = tr.find_all("td")
        if len(tds) < 4:
            continue

        date_str = tds[0].get_text(strip=True)
        weather   = tds[1].get_text(" / ", strip=True)   # 白天/夜间，用 " / " 连接

        # 气温：从 span.temp-high / span.temp-low 取，更精准
        high_tag = tds[2].find("span", class_="temp-high")
        low_tag  = tds[2].find("span", class_="temp-low")
        high = high_tag.get_text(strip=True).replace("℃", "") if high_tag else ""
        low  = low_tag.get_text(strip=True).replace("℃", "")  if low_tag  else ""

        wind = tds[3].get_text(" / ", strip=True)

        records.append({
            "日期":        date_str,
            "天气状况":    weather,
            "最高气温(℃)": high,
            "最低气温(℃)": low,
            "风力风向":    wind,
        })

    df = pd.DataFrame(records)
    df["最高气温(℃)"] = pd.to_numeric(df["最高气温(℃)"], errors="coerce")
    df["最低气温(℃)"] = pd.to_numeric(df["最低气温(℃)"], errors="coerce")
    df.dropna(subset=["最高气温(℃)", "最低气温(℃)"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


if __name__ == "__main__":
    # 默认爬取上个月的完整数据
    now   = datetime.now()
    month = now.month - 1 if now.month > 1 else 12
    year  = now.year      if now.month > 1 else now.year - 1

    print(f"正在爬取北京 {year}年{month:02d}月 天气数据...")
    df = fetch_beijing_weather(year, month)

    # ── 控制台打印完整表格 ─────────────────────────────────────
    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)
    pd.set_option("display.max_rows", 60)
    pd.set_option("display.width", 140)
    print(f"\n北京 {year}年{month:02d}月 天气数据（共 {len(df)} 天）\n")
    print(df.to_string(index=False))

    # ── 月度统计摘要 ──────────────────────────────────────────
    print("\n── 月度统计 ──")
    print(f"最高气温  均值: {df['最高气温(℃)'].mean():.1f}℃  "
          f"最高: {df['最高气温(℃)'].max():.0f}℃  "
          f"最低: {df['最高气温(℃)'].min():.0f}℃")
    print(f"最低气温  均值: {df['最低气温(℃)'].mean():.1f}℃  "
          f"最高: {df['最低气温(℃)'].max():.0f}℃  "
          f"最低: {df['最低气温(℃)'].min():.0f}℃")

    # ── 保存 CSV ──────────────────────────────────────────────
    out_path = (
        f"E:/self_code/self_learning_py_np_pd_ml/06_ml/"
        f"beijing_weather_{year}{month:02d}.csv"
    )
    df.to_csv(out_path, index=False, encoding="utf-8-sig")
    print(f"\n数据已保存至: {out_path}")
