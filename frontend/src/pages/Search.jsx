import { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';

function SearchPage() {
  const [query, setQuery] = useState('');
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [author, setAuthor] = useState('');
  const [results, setResults] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [categories, setCategories] = useState(["POLITICS", "WELLNESS", "ENTERTAINMENT", "TRAVEL", "STYLE"]);

  const resultsPerPage = 1000;

  const handleSearch = async () => {
    try {
      const params = new URLSearchParams();
      params.append("q", query);
      if (author) params.append("author", author);
      selectedCategories.forEach(cat => params.append("category", cat));

      const res = await axios.get(`http://127.0.0.1:8000/search_with_filters?${params.toString()}`);
      setResults(res.data.results);
      setCurrentPage(1);
    } catch (err) {
      console.error(err);
    }
  };

  const handleCategoryChange = (e) => {
    const value = e.target.value;
    if (e.target.checked) {
      setSelectedCategories((prev) => [...prev, value]);
    } else {
      setSelectedCategories((prev) => prev.filter((c) => c !== value));
    }
  };

  const paginatedResults = results.slice((currentPage - 1) * resultsPerPage, currentPage * resultsPerPage);

  return (
    <div>
      <main>
        <section className="search-input-section">
          <div className="search-input-container">
            <img
              src="https://media.geeksforgeeks.org/wp-content/uploads/20240122040847/search.png"
              alt="search"
              className="gsb"
            />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Rechercher ici"
              className="search-input"
            />
          </div>

          <img
            src="https://media.geeksforgeeks.org/wp-content/uploads/20240120153531/google-voice.png"
            alt="Mic"
            className="mic-icon"
            type="button"
            onClick={handleSearch}
          />
        </section>

        <section className="buttons-section">
          {categories.map((cat, index) => (
            <span className="pe-3" key={index}>
              <input
                type="checkbox"
                id={`category-${index}`}
                value={cat}
                checked={selectedCategories.includes(cat)}
                onChange={handleCategoryChange}
              />
              <label htmlFor={`category-${index}`} className="text-black">
                {cat}
              </label>
            </span>
          ))}
        </section>
      </main>

      <div className="clearfix mt-4">
        <ul className="xsearch-items list-unstyled">
          {paginatedResults.map((item, index) => (
            <li className="search-item d-flex mb-4" key={index}>
              <div className="search-item-content">
                <h3 className="search-item-caption">
                  <a href={item.link} target="_blank" rel="noopener noreferrer">{item.headline}</a>
                </h3>

                <div className="search-item-meta mb-2">
                  <ul className="list-inline">
                    <li className="list-inline-item text-muted">{item.date}</li>
                    <li className="list-inline-item">
                      <span>Catégorie</span>
                    </li>
                    <li className="list-inline-item pr-0">:</li>
                    <li className="list-inline-item pl-0">
                      {item.category && <a href="#">{item.category}</a>}
                    </li>
                  </ul>
                </div>

                <div>
                  {item.short_description || "No description available."}
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default SearchPage;
