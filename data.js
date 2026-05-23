// website-portfolio/data.js

// 1. Thông tin định danh cá nhân & Định hướng giải pháp
export const profileData = {
    name: "Nancy Nguyen",
    fullName: "Nguyen Ngo Uyen Ngoc",
    role: "Operations & Automation Specialist",
    bio: "Kỹ sư tối ưu hóa vận hành và tự động hóa quy trình với nền tảng chuyên sâu về Tài chính - Kế toán. Chuyên xây dựng hệ thống tự trị xử lý dữ liệu và cấu trúc giải pháp AI Ops cho doanh nghiệp.",
    skills: [
        "Python (Pandas, Gradio)", "n8n Automation", "UiPath RPA", 
        "Power BI / DAX", "Power Query", "IFRS & VAS Frameworks"
    ],
    contact: {
        email: "nancy.nguyen@example.com", // Thay thế bằng email chính thức của bạn
        linkedin: "https://linkedin.com/in/nancy-nguyen",
        github: "https://github.com/nngouyenngoc913",
        location: "Ho Chi Minh City, Vietnam"
    }
};

// 2. Cấu trúc dữ liệu danh mục sản phẩm chính
export const siteData = {
    projects: {
        title: "Core Architecture",
        subtitle: "Hệ thống kiến trúc dữ liệu và giải pháp chuyển đổi số tài chính.",
        items: [
            { 
                id: "p1",
                title: "Company report - FMCG", 
                description: "Ứng dụng trực quan hóa và phân tích sâu hiệu suất biên lợi nhuận, dòng tiền và biến động cổ phiếu ngành hàng tiêu dùng nhanh trên các sàn giao dịch niêm yết.", 
                link: "https://vnmproject1.netlify.app/", 
                image: "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800", 
                tag: "Analysis",
                techStack: ["Power BI", "DAX", "Financial Modeling"]
            },
            { 
                id: "p2",
                title: "Double-entry Logic", 
                description: "Kiến trúc quy trình hạch toán tự động tích hợp mô hình phân tích mẫu (Pattern Recognition) và AI gợi ý phân loại định khoản tự động cho hệ thống kế toán doanh nghiệp.", 
                link: "https://canva.link/41sfnm3pnld703v", 
                image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800", 
                tag: "Systems",
                techStack: ["AI Logic", "Process Mapping", "Accounting Workflow"]
            },
            { 
                id: "p3",
                title: "IFRS Hierarchy", 
                description: "Nền tảng tương tác trực quan sơ đồ cây logic cấu trúc Hệ thống chuẩn mực báo cáo tài chính quốc tế, hỗ trợ tra cứu phân cấp nhanh các chỉ tiêu tài chính.", 
                link: "https://nngouyenngoc913.github.io/ifrs-hierachy/", 
                image: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800", 
                tag: "IFRS",
                techStack: ["JavaScript", "Tailwind CSS", "Data Visualization"]
            },
            { 
                id: "p4",
                title: "IFRS library", 
                description: "Cơ sở dữ liệu tri thức mã nguồn mở tập trung, đồng bộ hệ thống văn bản quy phạm pháp luật kế toán bao gồm IFRS, VAS, các thông tư và nghị định hiện hành.", 
                link: "https://ifrs-vas.vercel.app/ifrs-16/", 
                image: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800", 
                tag: "IFRS",
                techStack: ["Next.js", "Markdown", "Knowledge Base"]
            } 
        ]
    },
    videos: {
        title: "Video Case Studies",
        subtitle: "Demo thực tế các luồng vận hành tự động và kiến trúc Agentic.",
        items: [
            { 
                id: "v1",
                title: "Agentic Workflows", 
                description: "Xây dựng hệ thống tự trị tối ưu hóa quy trình vận hành phòng tài chính, tự động xử lý đối chiếu công nợ thông qua kiến trúc AI Ops.", 
                videoId: "RXbkd8viWtg", 
                tag: "AI Ops",
                platform: "YouTube"
            },
            { 
                id: "v2",
                title: "SEO Automation", 
                description: "Thiết kế luồng tự động hóa nội dung trên n8n, tích hợp kỹ thuật cào dữ liệu web (Web Scraping) và tinh chỉnh prompt với OpenAI API.", 
                videoId: "w-JB9sCkvkQ", 
                tag: "Automation",
                platform: "YouTube"
            },
            { 
                id: "v3",
                title: "RPA ứng dụng", 
                description: "Phát triển cấu trúc webhook kết nối luồng xử lý n8n với Telegram Bot để tự động tổng hợp, phân loại và cảnh báo tin tức thị trường tài chính theo thời gian thực.", 
                videoId: "8PxQhfB6SXQ", 
                tag: "Automation",
                platform: "YouTube"
            }
        ]
    },
    blog: {
        title: "Blog & Insights",
        subtitle: "Ghi chép chuyên sâu về tư duy phân tích hệ thống và công nghệ tài chính.",
        items: [
            { 
                id: "b1",
                title: "Ứng dụng AI & Pattern Recognition trong Kế toán", 
                description: "Phân tích phương pháp ứng dụng mô hình cây quyết định (Decision Tree) và mô hình ngôn ngữ lớn để tự động hóa định khoản, tối ưu hóa quy trình nhập liệu thủ công.", 
                image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800", 
                tag: "AI & Data",
                file: "posts/md1.md",
                date: "2026-04"
            }, 
            {
                id: "b2",
                title: "Bảng cân đối kế toán - Một số insights", 
                description: "Giải mã nguồn gốc dòng tiền, cấu trúc tài sản và các điểm cốt lõi cần lưu ý khi phân tích sức khỏe tài chính của doanh nghiệp dưới góc nhìn quản trị.", 
                image: "https://images.unsplash.com/photo-1543286386-7a395010df6c?w=800", 
                tag: "BCTC",
                file: "posts/md2.md",
                date: "2026-05"
            }
        ]
    }
};

// 3. Danh sách bộ lọc phục vụ cho Filter Logic trên giao diện UI
export const filterTags = {
    projects: ["All", "Analysis", "Systems", "IFRS"],
    videos: ["All", "AI Ops", "Automation"],
    blog: ["All", "AI & Data", "BCTC"]
};
