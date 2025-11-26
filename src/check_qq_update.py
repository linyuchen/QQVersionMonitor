import re

import httpx

from bs4 import BeautifulSoup

from .qq_download_link import QQDownloadLinkManager

url = "https://docs.qq.com/doc/DVXNoRlpKaWhEY015?nlc=1"

class QQNTVersionMonitor:
    current_version = ''

    async def init(self):
        await self.get_new_version()

    async def get_version(self):
        client = httpx.AsyncClient()
        response = await client.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch the page: {response.text}")
        content = response.text
        download_links = re.findall('https://dldir.+?qqfile/qq/QQNT/[^<]+', content)
        if not download_links:
            return None, ''
        soup = BeautifulSoup(content)
        texts = [tag.get_text(strip=True) for tag in soup.find_all('text')]
        texts = '\n'.join(texts)
        feature_start_pos = texts.rfind('【版本特性】')
        lnk_start_pos = texts.rfind("【下载链接】")
        change_log_content = texts[feature_start_pos:]
        if lnk_start_pos != -1:
            if lnk_start_pos > feature_start_pos:
                change_log_content = change_log_content[:lnk_start_pos]
            else:
                change_log_content = change_log_content[lnk_start_pos:]

        if '【下载地址】' in change_log_content:
            change_log_content = change_log_content[:change_log_content.rfind('【下载地址】')]

        version = re.findall(r'(\d{5})_', download_links[0])[0]
        text = f'QQNT {version}\n{change_log_content}\n\n'
        links_manager = QQDownloadLinkManager()
        for link in download_links:
            name = links_manager.add_link(link).description
            if name:
                text += f'{name}: {link}\n'
        return version, text, links_manager

    async def get_new_version(self) -> tuple[str | None, str, QQDownloadLinkManager | None]:
        try:
            v, change_log, links = await self.get_version()
        except Exception as e:
            return None, '', None
        if v and v > self.current_version:
            self.current_version = v
            return v, change_log, links
        return None, '', None


qqnt_version_monitor = QQNTVersionMonitor()


