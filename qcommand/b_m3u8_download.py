# -*- coding: utf-8 -*-
# flake8: noqa
import m3u8, logging
from urllib.parse import quote
from bdownload import Batch_download
from command_threadpool import SimpleThreadPool
from util import to_unicode

logger = logging.getLogger("qcommand")


class B_m3u8_download(object):
    def __init__(self, access_key, secret_key, cdn_domain, input_file, save_path, http_headers, private,
                 successfile,
                 failurefile, thread_count):
        self.access_key = access_key
        self.secret_key = secret_key
        self.input_file = input_file
        self.save_path = save_path
        self.cdn_domain = cdn_domain
        self.private = private
        self._http_headers = http_headers
        self.thread_count = thread_count
        self.successfile = successfile
        self.failurefile = failurefile

    def get_ts_list(self, file_url):
        ts_list = m3u8.load(file_url)
        return ts_list

    def file_url(self, filename):
        if self.private:
            file_url = Batch_download.private_downloadurl(filename)
        else:
            file_url = "http://{0}/{1}".format(self.cdn_domain, quote(filename, safe="/"))
        return file_url

    def batch_m3u8_download(self):
        self._inner_threadpool = SimpleThreadPool(self.thread_count)
        try:
            with open(self.input_file, "r") as f:
                for filename in f:
                    if "," in filename:
                        filename = filename.split(",")[0]
                    else:
                        filename = filename.rstrip()
                    file_m3u8_url = self.file_url(filename)
                    try:
                        hls_list = self.get_ts_list(file_m3u8_url)
                        hls_list.append(filename)
                        for file_name in hls_list:
                            file_url = self.file_url(file_name)
                            self._inner_threadpool.add_task(Batch_download.download, file_url, filename, self.save_path,
                                                            self._http_headers,
                                                            self.successfile, self.failurefile)

                    except Exception as e:
                        logger.warn(to_unicode(e))
                self._inner_threadpool.wait_completion()
                result = self._inner_threadpool.get_result()
                return print(result)
        except Exception as e:
            logger.warn(to_unicode(e))
            raise e