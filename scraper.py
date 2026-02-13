<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HR-Headhunt | XML Job Fetcher</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600;700&display=swap');
        body { font-family: 'Lexend', sans-serif; background-color: #f0f4f8; }
        .source-tag { font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; font-weight: bold; text-transform: uppercase; }
        /* Hiệu ứng hover cho thẻ Job */
        .job-card { transition: all 0.3s ease; border: 1px solid transparent; }
        .job-card:hover { transform: translateY(-5px); border-color: #6366f1; background-color: #ffffff; }
    </style>
</head>
<body class="p-4 md:p-8">

    <div class="max-w-5xl mx-auto">
        <header class="mb-8 flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div>
                <h1 class="text-3xl font-black text-indigo-900 tracking-tight">Friendly-Headhunt <span class="text-indigo-500">XML</span></h1>
                <p class="text-slate-500 font-medium">Hệ thống quét dữ liệu từ DuckDuckGo & Boolean Search</p>
            </div>
            <div class="flex gap-2">
                <span class="source-tag bg-blue-100 text-blue-600">DuckDuckGo</span>
                <span class="source-tag bg-orange-100 text-orange-600">Careerjet Source</span>
                <span class="source-tag bg-green-100 text-green-600">Live XML</span>
            </div>
        </header>

        <div class="grid grid-cols-1 gap-6">
            <div class="bg-white rounded-3xl shadow-xl border border-slate-200 p-6 md:p-8">
                <div class="mb-6">
                    <label class="block text-sm font-bold text-slate-700 mb-2 underline decoration-indigo-300">Nhập từ khóa tìm kiếm (Sử dụng Boolean nếu cần)</label>
                    <input type="text" id="custom_keyword" placeholder="Ví dụ: Accountant Junior Part-time" 
                           class="w-full p-4 bg-slate-50 border-2 border-indigo-50 rounded-2xl outline-none focus:border-indigo-500 transition-all font-semibold text-indigo-900 shadow-inner">
                    <p class="text-[10px] text-slate-400 mt-2 italic px-2">* Lưu ý: Nhấn Start để đọc dữ liệu từ lần cào gần nhất của GitHub Actions.</p>
                </div>

                <button id="search_btn" class="w-full py-4 bg-slate-900 hover:bg-indigo-600 text-white font-black rounded-2xl shadow-lg transition-all flex items-center justify-center gap-3 tracking-widest uppercase">
                    <i class="fas fa-project-diagram"></i> Start XML Parsing
                </button>
            </div>

            <div class="bg-[#1e293b] rounded-3xl p-6 shadow-2xl relative">
                <div class="flex items-center justify-between mb-6 px-2">
                    <span class="text-xs font-bold text-indigo-400 uppercase tracking-widest"><i class="fas fa-terminal mr-2"></i>Live Job Cards</span>
                    <button onclick="copyRawXML()" class="text-[10px] bg-slate-700 hover:bg-slate-600 text-white px-3 py-1.5 rounded-lg font-bold transition-all uppercase">
                        <i class="fas fa-code mr-1"></i> Copy Raw XML
                    </button>
                </div>
                
                <div id="job_container" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <p class="text-slate-500 font-mono text-sm col-span-full text-center py-10">Chưa có dữ liệu. Nhấn nút phía trên để bắt đầu...</p>
                </div>

                <textarea id="raw_xml_output" class="hidden"></textarea>
            </div>
        </div>
    </div>

    <script>
        const searchBtn = document.getElementById('search_btn');
        const jobContainer = document.getElementById('job_container');
        const rawXmlOutput = document.getElementById('raw_xml_output');

        searchBtn.addEventListener('click', () => {
            searchBtn.disabled = true;
            searchBtn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Parsing XML...`;

            fetch('data.xml')
                .then(res => {
                    if (!res.ok) throw new Error("File XML chưa tồn tại");
                    return res.text();
                })
                .then(xmlString => {
                    rawXmlOutput.value = xmlString; // Lưu trữ XML thô để copy
                    const parser = new DOMParser();
                    const xmlDoc = parser.parseFromString(xmlString, "text/xml");
                    
                    const jobs = xmlDoc.getElementsByTagName("job");
                    const status = xmlDoc.getElementsByTagName("status")[0]?.textContent;

                    jobContainer.innerHTML = ''; // Xóa nội dung cũ

                    if (status === "Success" || jobs.length > 0) {
                        Array.from(jobs).forEach(job => {
                            const title = job.getElementsByTagName("title")[0]?.textContent || "N/A";
                            const company = job.getElementsByTagName("company")[0]?.textContent || "N/A";
                            const location = job.getElementsByTagName("location")[0]?.textContent || "N/A";
                            const link = job.getElementsByTagName("link")[0]?.textContent || "#";

                            jobContainer.innerHTML += `
                                <div class="job-card bg-slate-800/50 p-5 rounded-2xl border border-slate-700">
                                    <h3 class="text-emerald-400 font-bold text-lg mb-2 line-clamp-1">${title}</h3>
                                    <div class="text-slate-300 text-sm space-y-1 mb-4">
                                        <p><i class="fas fa-building text-indigo-400 mr-2"></i>${company}</p>
                                        <p><i class="fas fa-map-marker-alt text-rose-400 mr-2"></i>${location}</p>
                                    </div>
                                    <a href="${link}" target="_blank" class="inline-block w-full text-center py-2 bg-indigo-500/10 hover:bg-indigo-500 text-indigo-400 hover:text-white rounded-xl font-bold text-xs transition-all uppercase tracking-tighter">
                                        View Details <i class="fas fa-external-link-alt ml-1"></i>
                                    </a>
                                </div>
                            `;
                        });
                    } else {
                        jobContainer.innerHTML = `<p class="text-rose-400 font-mono text-sm col-span-full">Status: ${status || 'No jobs found'}</p>`;
                    }
                    resetButton();
                })
                .catch(err => {
                    jobContainer.innerHTML = `<p class="text-rose-400 font-mono text-sm col-span-full">Lỗi: ${err.message}</p>`;
                    resetButton();
                });
        });

        function resetButton() {
            searchBtn.disabled = false;
            searchBtn.innerHTML = `<i class="fas fa-project-diagram"></i> Start XML Parsing`;
        }

        function copyRawXML() {
            if (!rawXmlOutput.value) {
                alert('Chưa có dữ liệu XML!');
                return;
            }
            rawXmlOutput.select();
            document.execCommand('copy');
            alert('Đã sao chép nội dung XML thô!');
        }
    </script>
</body>
</html>
